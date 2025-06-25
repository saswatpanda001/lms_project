from django.contrib import admin
from .models import ClassName, Department, Course, CourseOffering, Enrollment, Section,ClassSection,CurrentAttendance,ArchivedAttendance,ClassSchedule,PeriodSlot


admin.site.register(ClassName)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(CourseOffering)
admin.site.register(Enrollment)
admin.site.register(Section)
admin.site.register(ClassSection)
admin.site.register(CurrentAttendance)
admin.site.register(ArchivedAttendance)
admin.site.register(ClassSchedule)
admin.site.register(PeriodSlot)

