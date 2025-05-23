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
    UserProfileView
)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
]