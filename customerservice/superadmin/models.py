from django.db import models
from django.utils import timezone

class AdminInvite(models.Model):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=12, unique=True)
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.email} - {'Used' if self.used else 'Pending'}"
