from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager
from .helpers import create_project_icon_path


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Project(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)
    icon_path = models.ImageField(upload_to=create_project_icon_path)
    deadline = models.DateField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
