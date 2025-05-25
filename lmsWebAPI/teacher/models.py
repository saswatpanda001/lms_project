from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from academics.models import Department


class TeacherProfile(models.Model):
   
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='teacher_profile',
        verbose_name=_('user account')
    )
    
    # Personal Information
    bio = models.TextField(
        _('biography'),
        blank=True,null=True,
        help_text=_('A short professional biography')
    )
    profile_picture = models.ImageField(
        _('profile picture'),
        upload_to='teachers/profile_pictures/',
        blank=True,
        null=True
    )
    
    # Professional Information
    hire_date = models.DateField(
        _('date hired'),
        help_text=_('Date when the teacher was hired'),blank=True,null=True,
    )
  
    years_of_experience = models.PositiveSmallIntegerField(
        _('years of experience'),
        validators=[MinValueValidator(0), MaxValueValidator(50)],
        default=0,blank=True,null=True,
    )
    
    # Department Information
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teachers',
        verbose_name=_('department')
    )
    specialization = models.CharField(
        _('specialization'),
        max_length=100,
        help_text=_('Primary subject or field of expertise'),blank=True,null=True,
    )
   
    
    # Contact Information
    office_location = models.CharField(
        _('office location'),
        max_length=50,
        blank=True,null=True,
    )
   
 
    is_active = models.BooleanField(
        _('active status'),
        default=True,
        help_text=_('Designates whether this teacher is currently active')
    )
    notes = models.TextField(
        _('administrative notes'),
       blank=True,null=True,
        help_text=_('Internal notes about the teacher')
    )
    
    # Timestamps
    created_at = models.DateTimeField(
        _('created at'),
        auto_now_add=True,blank=True,null=True,
    )
    updated_at = models.DateTimeField(
        _('updated at'),
        auto_now=True,blank=True,null=True,
    )

 
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.get_employment_type_display()})"
    
   