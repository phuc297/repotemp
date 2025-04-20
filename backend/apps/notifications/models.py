from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.posts.models import Post
from apps.users.models import Profile


class Notification(models.Model):
    recipient = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    related_object = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Notification to {self.recipient}: {self.message}"
