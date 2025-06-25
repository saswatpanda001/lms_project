from datetime import datetime
import random

from django.conf import settings
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.mail import send_mail
from django.middleware.csrf import get_token

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import PasswordResetOTP
from .serializers import UserSerializer
from authentication.dual_auth import CookieJWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, TokenError



class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []  

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'error': 'Username and password required'}, status=400)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid credentials'}, status=401)

        # Generate tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        print(access_token)

        # Prepare response data (exclude sensitive info)
        response_data = {
            'status': 'success',
            'user': {
                'user_id': user.id,
                'email': user.email,
                'user_name': user.username,
                'role': user.role,
            
                
            }
        }

        response = Response(response_data)

        # Calculate cookie expiration dates
        access_expires = datetime.now() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        refresh_expires = datetime.now() + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']

        # Set HTTP-only cookies
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=access_token,
            expires=access_expires,
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=True,
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
        )
        
        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            expires=refresh_expires,
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=True,
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
        )
        
        # Set CSRF token for subsequent requests
        get_token(request)

        # Debug logging (optional)
        print(f"Login successful for user: {user.username} (ID: {user.id})")
        print(f"Access token expires: {access_expires}")
        print(f"Refresh token expires: {refresh_expires}")
        print(user)

        return response
    


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Blacklist refresh token if exists
            refresh_token = request.COOKIES.get('refresh_token')
            if refresh_token:
                try:
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                except TokenError:
                    pass  # Invalid or already blacklisted token, ignore

        except Exception as e:
            print(f"Logout error: {str(e)}")

        response = Response({'status': 'success'})

        # Clear all auth cookies
        cookies_to_delete = [
            settings.SIMPLE_JWT['AUTH_COOKIE'],
            'refresh_token',
            'access_token',
            'csrf_token'
        ]

        for cookie in cookies_to_delete:
            response.delete_cookie(
                cookie,
                path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
                domain=settings.SIMPLE_JWT['AUTH_COOKIE_DOMAIN'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
              
            )

        return response

class VerifyAuthView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CookieJWTAuthentication]

    def get(self, request):
        return Response({
            'user': {
                'id': request.user.id,
                'email': request.user.email,
                'username': request.user.username,
                'role': request.user.role
            }
        })


class RefreshTokenView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not refresh_token:
            return Response({'error': 'Refresh token missing'}, status=400)
        
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)
            
            response = Response({'status': 'token refreshed'})
            
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=access_token,
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=True,
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
                path=settings.SIMPLE_JWT['AUTH_COOKIE_PATH'],
            )
            
            return response
        except Exception as e:
            return Response({'error': str(e)}, status=401)
        



class UserProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)




class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'status': 'success',
                    'user': serializer.data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











User = get_user_model()

class SendOTPView(APIView):
    permission_classes = []  # Allow unauthenticated access

    def post(self, request):
        username = request.data.get('username')
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Generate 6-digit OTP
        otp = str(random.randint(100000, 999999))
        
        # Invalidate previous OTPs
        PasswordResetOTP.objects.filter(user=user).update(is_used=True)
        
        # Save new OTP
        PasswordResetOTP.objects.create(user=user, otp=otp)
        
        # Send email
        send_mail(
            'Password Reset OTP',
            f'Your OTP for password reset is: {otp}\nValid for 10 minutes.',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        
        return Response({'status': 'OTP sent to registered email'})

class VerifyOTPView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        otp = request.data.get('otp')
        
        try:
            user = User.objects.get(username=username)
            otp_record = PasswordResetOTP.objects.get(
                user=user,
                otp=otp,
                is_used=False,
            )
            
            if otp_record.is_expired:
                return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)
                
            return Response({'status': 'OTP verified'})
            
        except (User.DoesNotExist, PasswordResetOTP.DoesNotExist):
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        otp = request.data.get('otp')
        new_password = request.data.get('new_password')
        
        try:
            user = User.objects.get(username=username)
            otp_record = PasswordResetOTP.objects.get(
                user=user,
                otp=otp,
                is_used=False,
            )
            
            if otp_record.is_expired:
                return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)
                
            # Update password
            user.set_password(new_password)
            user.save()
            
            # Mark OTP as used
            otp_record.is_used = True
            otp_record.save()
            
            return Response({'status': 'Password reset successful'})
            
        except (User.DoesNotExist, PasswordResetOTP.DoesNotExist):
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
        