from rest_framework import serializers
from .models import Course, ClassSchedule, CourseOffering, PeriodSlot, TeacherProfile, ClassSection




# PeriodSlot Serializer
class PeriodSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodSlot
        fields = ['id', 'name', 'start_time', 'end_time']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'code']




# CourseOffering Serializer
class CourseOfferingSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = CourseOffering
        fields = ['id', 'course']


# TeacherProfile Serializer
class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ['id', 'username']  # Add fields as needed


# ClassSection Serializer
class ClassSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSection
        fields = ['id', 'name']


class ClassScheduleSerializer(serializers.ModelSerializer):
    class_info = ClassSectionSerializer()
    period = PeriodSlotSerializer()
    course_offering = CourseOfferingSerializer()
    teacher = TeacherProfileSerializer()


    class Meta:
        model = ClassSchedule
        fields = '__all__'  
