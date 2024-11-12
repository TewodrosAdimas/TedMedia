# notifications/urls.py

from django.urls import path
from .views import get_notifications, mark_notification_read

urlpatterns = [
    path('notifications/', get_notifications, name='get_notifications'),
    path('notifications/read/<int:notification_id>/', mark_notification_read, name='mark_notification_read'),
]
