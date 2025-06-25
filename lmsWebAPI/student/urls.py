from django.contrib import admin
from django.urls import path,include
from .views import StudentProfileAPIView
app_name = "student"


urlpatterns = [
    path(
        'api/profile/', StudentProfileAPIView.as_view(),name='student-profile'
    ),
]
