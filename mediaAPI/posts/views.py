from django.contrib.contenttypes.models import ContentType
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .permissions import IsAuthorOrReadOnly
from notifications.models import Notification




# Filter class for posts
class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains', label='Title contains')
    content = filters.CharFilter(lookup_expr='icontains', label='Content contains')

    class Meta:
        model = Post
        fields = ['title', 'content']
        
@api_view(['POST'])
def like_post(request, post_id):
    """Like a post and generate a notification for the post's author."""
    post = get_object_or_404(Post, id=post_id)

    if Like.objects.filter(post=post, user=request.user).exists():
        return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create the like
    Like.objects.create(post=post, user=request.user)

    # Create notification
    content_type = ContentType.objects.get_for_model(post)
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        target_content_type=content_type,
        target_object_id=post.id
    )

    return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def unlike_post(request, post_id):
    """Unlike a post."""
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(post=post, user=request.user).first()

    if not like:
        return Response({"detail": "You have not liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({"detail": "Post unliked successfully."}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_post(request, post_id):
    """Comment on a post and generate a notification for the post's author."""
    post = get_object_or_404(Post, id=post_id)
    content = request.data.get('content')

    if not content:
        return Response({"detail": "Content is required."}, status=status.HTTP_400_BAD_REQUEST)

    comment = Comment.objects.create(post=post, author=request.user, content=content)

    # Create notification
    content_type = ContentType.objects.get_for_model(comment)
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="commented on your post",
        target_content_type=content_type,
        target_object_id=comment.id
    )

    return Response({"detail": "Comment added successfully."}, status=status.HTTP_201_CREATED)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter

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
        post = serializer.validated_data['post']
        user = self.request.user

        if Like.objects.filter(post=post, user=user).exists():
            raise serializers.ValidationError("You have already liked this post.")
        
        serializer.save(user=user)
