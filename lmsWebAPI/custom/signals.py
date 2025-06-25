# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from student.models import StudentProfile
from teacher.models import TeacherProfile
User = get_user_model()


@receiver(post_save, sender= User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'student':
            StudentProfile.objects.create(user=instance,username=instance.username,email=instance.email)
        elif instance.role == 'teacher':
            TeacherProfile.objects.create(user=instance,username=instance.username,email=instance.email)