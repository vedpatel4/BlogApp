from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser, PermissionsMixin
)
from .managers import CustomUserManager;

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    # Use 'email' as the unique identifier for authentication
    USERNAME_FIELD = 'email'

    # Required fields when creating a user (via createsuperuser)
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email