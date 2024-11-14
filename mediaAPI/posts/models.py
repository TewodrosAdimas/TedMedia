from django.db import models
from django.conf import settings
from accounts.models import CustomUser


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
    

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')  # Ensures a user can like a post only once

    def __str__(self):
        return f"{self.user} liked {self.post}"
    



from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from .models import Post, Like
from django.contrib.auth.models import User
from notifications.models import Notification
@api_view(['POST'])
def like_post(request, post_id):
    """
    View to like a post.
    - Checks if the user is authenticated.
    - Prevents liking a post multiple times.
    - Generates a notification for the post owner.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

    # Prevent the user from liking the post multiple times
    if Like.objects.filter(post=post, user=request.user).exists():
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create the Like object
    like = Like.objects.create(post=post, user=request.user)

    # Generate notification for the post owner
    content_type = ContentType.objects.get_for_model(post)
    notification = Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        target_content_type=content_type,
        target_object_id=post.id
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def unlike_post(request, post_id):
    """
    View to unlike a post.
    - Checks if the user is authenticated.
    - Prevents unliking a post that hasn't been liked yet.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user has already liked the post
    like = Like.objects.filter(post=post, user=request.user).first()
    if not like:
        return Response({"detail": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete the Like object
    like.delete()

    return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)

