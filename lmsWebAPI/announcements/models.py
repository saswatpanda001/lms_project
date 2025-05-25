from django.db import models
from django.utils import timezone
from academics.models import ClassName, Section

class Announcements(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    for_all = models.BooleanField(blank=True, null=True)
    for_class = models.ManyToManyField(ClassName,blank=True, related_name="announcement_for_class")
    for_section = models.ManyToManyField(Section,blank=True,related_name="announcement_for_section")
    
    is_active = models.BooleanField(default=True,blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_on = models.DateTimeField(default=timezone.now,blank=True, null=True)


    def __str__(self):
        return str(self.title)
    
