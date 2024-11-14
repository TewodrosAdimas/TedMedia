from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileUpdateSerializer
from rest_framework.decorators import api_view, permission_classes
from notifications.models import Notification
from django.shortcuts import get_object_or_404
from .models import CustomUser

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    """
    Follow another user and generate a notification for the followed user.
    """
    user_to_follow = get_object_or_404(CustomUser, id=user_id)
    
    if user_to_follow == request.user:
        return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.user.following.filter(id=user_to_follow.id).exists():
        return Response({"message": "You already follow this user"}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.add(user_to_follow)

    # Create a notification for the followed user
    Notification.objects.create(
        recipient=user_to_follow,
        actor=request.user,
        verb="started following you"
    )

    return Response({"message": "You are now following this user"}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    """
    Unfollow a user.
    """
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
    
    if user_to_unfollow == request.user:
        return Response({"error": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)
    
    if not request.user.following.filter(id=user_to_unfollow.id).exists():
        return Response({"message": "You do not follow this user"}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.remove(user_to_unfollow)
    return Response({"message": "You have unfollowed this user"}, status=status.HTTP_200_OK)


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileUpdateSerializer  # Use the profile update serializer here
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user  # Return the current authenticated user


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
