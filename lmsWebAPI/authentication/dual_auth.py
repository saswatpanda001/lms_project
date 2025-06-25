
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.exceptions import TokenError
from django.utils import timezone

class CookieJWTAuthentication(JWTAuthentication):
    """
    JWT authentication that checks for tokens in cookies or headers
    with blacklist verification
    """
    def authenticate(self, request):
        # Try header-based auth first
        header_auth = super().authenticate(request)
        if header_auth:
            return header_auth
        
        # Fall back to cookie-based auth
        cookie_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        if not cookie_token:
            return None
            
        try:
            validated_token = self.get_validated_token(cookie_token)
            
            # Check if token is blacklisted
            jti = validated_token.get('jti')
            if jti and BlacklistedToken.objects.filter(token__jti=jti).exists():
                raise TokenError('Token is blacklisted')
                
            return self.get_user(validated_token), validated_token
            
        except TokenError as e:
            return None
        