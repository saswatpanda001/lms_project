from django.contrib import admin
from .models import Announcement,ContentType,CourseContent,Syllabus

admin.site.register(Announcement)
admin.site.register(ContentType)
admin.site.register(CourseContent)
admin.site.register(Syllabus)
