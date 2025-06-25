# urls.py
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from authentication.serializers import UserSerializer;

from authentication.views import (
    RegisterView,
    LoginView,
    LogoutView,
    UserProfileView,
    VerifyAuthView,SendOTPView, 
    VerifyOTPView, 
    ResetPasswordView
    
)



urlpatterns = [
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/verify/', VerifyAuthView.as_view(), name='verify-auth'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
    path('api/register/', RegisterView.as_view(), name='register'),

    path('api/forgot-password/send-otp/', SendOTPView.as_view()),
    path('api/forgot-password/verify-otp/', VerifyOTPView.as_view()),
    path('api/forgot-password/reset/', ResetPasswordView.as_view()),
 
]