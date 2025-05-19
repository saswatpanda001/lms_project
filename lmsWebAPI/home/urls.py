from django.contrib import admin
from django.urls import path,include
from home.views import (
    home,
    student_assignments,
    student_attendance,
    student_courses,
    student_dashboard,
    student_grades,
    student_timetable,
    teacher_analytics,
    teacher_assignments,
    teacher_course,
    teacher_dashboard,
    teacher_attendance,
    alumni,
    alumni_programs
)


app_name = "home"



urlpatterns = [
    path('', home, name='landing_page'),
    path('student/assignments', student_assignments, name='student_assignments'),
    path('student/attendance', student_attendance, name='student_attendance'),
    path('student/courses', student_courses, name='student_courses'),
    path('student/dashboard', student_dashboard, name='student_dashboard'),
    path('student/grades', student_grades, name='student_grades'),
    path('student/timetable', student_timetable, name='student_timetable'),
    path('teacher/analytics', teacher_analytics, name='teacher_analytics'),
    path('teacher/assignments', teacher_assignments, name='teacher_assignments'),
    path('teacher/course', teacher_course, name='teacher_course'),
    path('teacher/dashboard', teacher_dashboard, name='teacher_dashboard'),
    path('teacher/attendance', teacher_attendance, name='teacher_attendance'),
    path('alumni/profile', alumni, name='alumni'),
    path('alumni/programs', alumni_programs, name='alumni_programs'),
]

