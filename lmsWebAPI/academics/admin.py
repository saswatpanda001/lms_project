from django.contrib import admin
from .models import ClassName, Department, Course, CourseOffering, Enrollment, Section

admin.site.register(ClassName)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CourseOffering)
admin.site.register(Enrollment)
admin.site.register(Section)

