
from django.db import models
from django.contrib.auth import get_user_model
from teacher.models import TeacherProfile
from student.models import StudentProfile
User = get_user_model()
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=10, unique=True,blank=True, null=True)
    head = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, related_name='department_head',blank=True, null=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100,blank=True, null=True)
    code = models.CharField(max_length=10, unique=True,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True, null=True)
    credit_hours = models.PositiveSmallIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} ({self.code})"

class ClassName(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
 
    def __str__(self):
        return str(self.name)


class Section(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
 
    def __str__(self):
        return str(self.name)
    

class ClassSection(models.Model):
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ('class_name', 'section') 

    def save(self, *args, **kwargs):
        if not self.name and self.class_name and self.section:
            self.name = f"{self.class_name.name}-{self.section.name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else "Unnamed ClassSection"


    

class CourseOffering(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True, null=True)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL,blank=True, null=True)
    class_info = models.ForeignKey(ClassSection, on_delete=models.SET_NULL,blank=True, null=True)
    semester = models.CharField(max_length=20,blank=True, null=True)
    academic_year = models.CharField(max_length=20,blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    class Meta:
        unique_together = ('course', 'class_info', 'semester', 'academic_year')
    
    def __str__(self):
        return f"{self.course} - {self.class_info} ({self.semester} {self.academic_year})"

class Enrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE,blank=True, null=True)
    course_offering = models.ForeignKey(CourseOffering, on_delete=models.CASCADE,blank=True, null=True)
    enrollment_date = models.DateField(auto_now_add=True,blank=True, null=True)
    is_active = models.BooleanField(default=True,blank=True, null=True)
    
    class Meta:
        unique_together = ('student', 'course_offering')
    
    def __str__(self):
        return f"{self.student} enrolled in {self.course_offering}"

class CurrentAttendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
        ('E', 'Excused')
    ]

    student = models.ForeignKey('student.StudentProfile', on_delete=models.CASCADE, blank=True, null=True)
    course_offering = models.ForeignKey('academics.CourseOffering', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    marked_by = models.ForeignKey('teacher.TeacherProfile', on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('student', 'course_offering', 'date')
        indexes = [
            models.Index(fields=['student']),
            models.Index(fields=['date']),
            models.Index(fields=['course_offering']),
        ]
        ordering = ['-date']

    def __str__(self):
        student_name = getattr(self.student, 'username', 'Unknown')
        return f"{self.date} - {student_name} - {self.get_status_display()}"




class ArchivedAttendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
        ('E', 'Excused')
    ]

    student = models.ForeignKey('student.StudentProfile', on_delete=models.CASCADE, blank=True, null=True)
    course_offering = models.ForeignKey('academics.CourseOffering', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(default=timezone.now, blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    marked_by = models.ForeignKey('teacher.TeacherProfile', on_delete=models.SET_NULL, null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('student', 'course_offering', 'date')
        indexes = [
            models.Index(fields=['student']),
            models.Index(fields=['date']),
            models.Index(fields=['course_offering']),
        ]
        ordering = ['-date']

    def __str__(self):
        student_name = getattr(self.student, 'username', 'Unknown')
        return f"{self.date} - {student_name} - {self.get_status_display()}"


class PeriodSlot(models.Model):
    name = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.name} ({self.start_time} - {self.end_time})"



class ClassSchedule(models.Model):
    class_info = models.ForeignKey(ClassSection, on_delete=models.CASCADE,blank=True,null=True)
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
        ]
    )
    period = models.ForeignKey('PeriodSlot', on_delete=models.CASCADE)
    course_offering = models.ForeignKey('academics.CourseOffering', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teacher.TeacherProfile', on_delete=models.SET_NULL, null=True, blank=True)
    room = models.CharField(max_length=20, blank=True, null=True) 

    class Meta:
        unique_together = ('class_info', 'day_of_week', 'period')
        ordering = ['day_of_week', 'period__start_time']

    def __str__(self):
        return f"{self.class_info} - {self.day_of_week} - {self.period.name}"