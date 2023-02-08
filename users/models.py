from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default="domain@gmail.com")
    phone_number = models.IntegerField(default="0123456678")

    def __str__(self):
        return self.user.username
