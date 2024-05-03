from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=45, blank=True, null=True, help_text="Phone number")
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(default="users/default.png",upload_to="users/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)