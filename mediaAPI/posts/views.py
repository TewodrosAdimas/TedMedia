from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from django_filters import rest_framework as filters
from .models import Like
from .serializers import LikeSerializer
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification
from django.contrib.auth.models import User

@api_view(['POST'])
def like_post(request, post_id):
    """
    View to like a post.
    Generates a notification for the post's author.
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

    # Create a notification for the post's author
    content_type = ContentType.objects.get_for_model(post)
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        target_content_type=content_type,
        target_object_id=post.id
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def comment_post(request, post_id):
    """
    View to comment on a post.
    Generates a notification for the post's author.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

    content = request.data.get('content')
    if not content:
        return Response({"detail": "Content is required."}, status=status.HTTP_400_BAD_REQUEST)

    comment = Comment.objects.create(post=post, author=request.user, content=content)

    # Create a notification for the post's author
    content_type = ContentType.objects.get_for_model(comment)
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="commented on your post",
        target_content_type=content_type,
        target_object_id=comment.id
    )

    return Response({"detail": "Comment added successfully."}, status=status.HTTP_201_CREATED)


# Filter class for posts
class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains', label='Title contains')
    content = filters.CharFilter(lookup_expr='icontains', label='Content contains')

    class Meta:
        model = Post
        fields = ['title', 'content']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = (DjangoFilterBackend,)  # Add filtering backend
    filterset_class = PostFilter  # Use the custom PostFilter for filtering

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)




class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Ensure that the user cannot like a post multiple times
        post = serializer.validated_data['post']
        user = self.request.user
        if Like.objects.filter(post=post, user=user).exists():
            raise serializers.ValidationError("You have already liked this post.")
        serializer.save(user=user)
