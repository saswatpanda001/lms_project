from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer, ClassScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from academics.models import ClassSchedule

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_enrolled_courses(request):
    student_id = request.user.id
    courses = Course.objects.filter(
        courseoffering__enrollment__student_id=student_id,
        courseoffering__enrollment__is_active=True
    ).distinct()

    if not courses.exists():
        return Response({"detail": "No enrolled courses found."}, status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_class_schedule(request):
    schedule_data = ClassSchedule.objects.all()
    schedule_serializer = ClassScheduleSerializer(schedule_data, many=True)
    return Response(schedule_serializer.data, status=status.HTTP_200_OK)

