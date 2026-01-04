from django.db import models
from django.contrib.auth.models import AbstractUser
import random
import uuid
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    followers = models.PositiveIntegerField(default=0)

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"


class IdeaBlog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ideas")
    title = models.CharField(max_length=48)
    description = models.TextField(max_length=5012)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)