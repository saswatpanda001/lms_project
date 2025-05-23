from django.contrib import admin
from .models import Class, Department, Course, CourseOffering, Enrollment, Program

admin.site.register(Class)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CourseOffering)
admin.site.register(Enrollment)
admin.site.register(Program)

