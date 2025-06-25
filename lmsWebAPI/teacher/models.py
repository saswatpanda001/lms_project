from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _



class TeacherProfile(models.Model):
   
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='teacher_profile',
        verbose_name=_('user account')
    )
    username = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(blank=True,null=True)
    class_allocated = models.ManyToManyField('academics.CourseOffering', blank=True,null=True)
    
    
 
    
    def __str__(self):
        return str(self.username)
    
   