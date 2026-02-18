from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics, permissions

# Create your views here.

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): # type:ignore
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')