from django.urls import path
from .views import get_enrolled_courses, get_class_schedule

urlpatterns = [
    path('api/enrolled-courses', get_enrolled_courses),
    path('api/class-schedule', get_class_schedule),
]
