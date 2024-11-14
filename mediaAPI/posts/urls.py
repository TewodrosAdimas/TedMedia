from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet, like_post, unlike_post, UserFeedView

router = DefaultRouter()
router.register(r'likes', LikeViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('unlike/<int:post_id>/', unlike_post, name='unlike_post'),
    path('feed/', UserFeedView.as_view(), name='user-feed'),

]
