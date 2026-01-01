from django.db import models
from django.contrib.auth.models import AbstractUser
import random

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"