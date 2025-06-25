from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils import timezone


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    username = models.CharField(max_length=200,blank=True, null=True)
    current_class = models.ForeignKey('academics.ClassSection', on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    enrollment_date = models.DateField(blank=True, null=True)
    expected_graduation = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At',blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Last Updated',blank=True, null=True)
    
    def __str__(self):
        return f"Student Profile: {self.username}"

