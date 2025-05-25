from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    enrollment_date = models.DateField(blank=True, null=True)
    expected_graduation = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At',blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated',blank=True, null=True)
    
    def __str__(self):
        return f"Student Profile: {self.user.get_full_name()}"

