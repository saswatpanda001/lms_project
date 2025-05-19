from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'landing.html')

def student_assignments(request):
    return render(request, 'student_assignment.html')

def student_attendance(request):
    return render(request, 'student_attendance.html')

def student_courses(request):
    return render(request, 'student_courses.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def student_grades(request):
    return render(request, 'student_grades.html')

def student_timetable(request):
    return render(request, 'student_timetable.html')

def teacher_analytics(request):
    return render(request, 'teacher_analytics.html')

def teacher_assignments(request):
    return render(request, 'teacher_assignments.html')

def teacher_course(request):
    return render(request, 'teacher_course.html')

def teacher_dashboard(request):
    return render(request, 'teacher_dashboard.html')

def teacher_attendance(request):
    return render(request, 'teacher_attendance.html')

def alumni(request):
    return render(request, 'alumni.html')


def alumni_programs(request):
    return render(request, 'alumni_programs.html')

