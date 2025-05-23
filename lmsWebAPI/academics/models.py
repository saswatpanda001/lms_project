
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Department(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=10, unique=True,blank=True, null=True)
    head = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='department_head',blank=True, null=True)
    
    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=10, unique=True,blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True, null=True)
    duration = models.PositiveSmallIntegerField(help_text="Duration in years",blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Class(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE,blank=True, null=True)
    academic_year = models.CharField(max_length=20,blank=True, null=True)
    class_teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.program} ({self.academic_year})"

class Course(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=10, unique=True,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True, null=True)
    credit_hours = models.PositiveSmallIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} ({self.code})"

class CourseOffering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    class_info = models.ForeignKey(Class, on_delete=models.CASCADE,blank=True, null=True)
    semester = models.CharField(max_length=20,blank=True, null=True)
    academic_year = models.CharField(max_length=20,blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    class Meta:
        unique_together = ('course', 'class_info', 'semester', 'academic_year')
    
    def __str__(self):
        return f"{self.course} - {self.class_info} ({self.semester} {self.academic_year})"

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE,blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True,blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    
    class Meta:
        unique_together = ('student', 'course_offering')
    
    def __str__(self):
        return f"{self.student} enrolled in {self.course_offering}"