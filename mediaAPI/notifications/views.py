# notifications/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification

@api_view(['POST'])
def mark_notification_read(request, notification_id):
    """
    View to mark a notification as read.
    """
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        # Fetch the notification for the authenticated user
        notification = Notification.objects.get(id=notification_id, recipient=request.user)
    except Notification.DoesNotExist:
        return Response({"detail": "Notification not found."}, status=status.HTTP_404_NOT_FOUND)

    # Mark the notification as read
    notification.is_read = True
    notification.save()

    return Response({"detail": "Notification marked as read."}, status=status.HTTP_200_OK)
