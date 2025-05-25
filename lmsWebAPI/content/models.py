from django.db import models
from academics.models import CourseOffering
from django.contrib.auth import get_user_model
User = get_user_model()
from academics.models import Department

class Syllabus(models.Model):
    course_offering = models.OneToOneField(CourseOffering, on_delete=models.CASCADE, related_name='syllabus',blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True,blank=True, null=True)
    
    def __str__(self):
        return f"Syllabus for {self.course_offering}"

class ContentType(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.name

class CourseContent(models.Model):
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, related_name='contents',blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL,blank=True, null=True)
    file = models.FileField(upload_to='course_contents/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True)
    is_published = models.BooleanField(default=False,blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.course_offering}"

class Announcement(models.Model):
    COURSE = 'CO'
    SCHOOL = 'SC'
    DEPARTMENT = 'DE'
    
    SCOPE_CHOICES = [
        (COURSE, 'Course'),
        (SCHOOL, 'School'),
        (DEPARTMENT, 'Department'),
    ]
    
    title = models.CharField(max_length=200,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    scope = models.CharField(max_length=2, choices=SCOPE_CHOICES,blank=True, null=True)
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    is_pinned = models.BooleanField(default=False,blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title