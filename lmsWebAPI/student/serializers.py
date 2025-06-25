# serializers.py
from rest_framework import serializers
from .models import StudentProfile
from django.contrib.auth.models import User

class StudentProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = StudentProfile
        fields = [
            'username', 'email', 'enrollment_date', 
            'expected_graduation', 'first_name', 'last_name',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def update(self, instance, validated_data):
        # Handle nested User model updates
        user_data = validated_data.pop('user', {})
        user = instance.user
        
        for attr, value in user_data.items():
            setattr(user, attr, value)
        user.save()
        
        return super().update(instance, validated_data)
