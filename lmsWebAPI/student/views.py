

# views.py
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import StudentProfile
from .serializers import StudentProfileSerializer
from django.shortcuts import get_object_or_404

class StudentProfileAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        data = StudentProfile.objects.all()
        return get_object_or_404(
            data
        )
    