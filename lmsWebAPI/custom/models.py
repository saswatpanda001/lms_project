from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('management', 'Management'),
        ('admin', 'Admin'),
        
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, blank=True, null=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
