from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework.permissions import BasePermission

from .serializers import GroupSerializer, CreateUserSerializer, \
    UpdateUserSerializer, SetupPasswordSerializer

from dj_rest_auth.views import LoginView
from django.conf import settings
from django.utils import timezone
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.settings import api_settings as jwt_settings


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and
                    request.user.groups.filter(name__in=settings.STAFF_GROUPS).exists())


class Login(LoginView):
    authentication_classes = []

    def get_response(self):
        response = super().get_response()
        if getattr(settings, "REST_USE_JWT", False):
            cookie_name = getattr(settings, "JWT_AUTH_COOKIE", None)
            refresh_cookie_name = getattr(settings, "JWT_AUTH_REFRESH_COOKIE", None)
            refresh_cookie_path = getattr(settings, "JWT_AUTH_REFRESH_COOKIE_PATH", "/")
            cookie_secure = getattr(settings, "JWT_AUTH_SECURE", False)
            cookie_httponly = getattr(settings, "JWT_AUTH_HTTPONLY", False)
            cookie_samesite = getattr(settings, "JWT_AUTH_SAMESITE", "Lax")

            # read domain from django settings
            cookie_domain = getattr(settings, "SESSION_COOKIE_DOMAIN", None)
            access_token_expiration = (timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME)
            refresh_token_expiration = (timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME)
            if cookie_name:
                response.set_cookie(
                    cookie_name,
                    self.access_token,
                    expires=access_token_expiration,
                    secure=cookie_secure,
                    domain=cookie_domain,
                    httponly=cookie_httponly,
                    samesite=cookie_samesite,
                ),

            if refresh_cookie_name:
                response.set_cookie(
                    refresh_cookie_name,
                    self.refresh_token,
                    expires=refresh_token_expiration,
                    secure=cookie_secure,
                    domain=cookie_domain,
                    httponly=cookie_httponly,
                    samesite=cookie_samesite,
                    path=refresh_cookie_path,
                )
        return response

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RefreshToken(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        cookie_name = getattr(settings, "JWT_AUTH_COOKIE", None)
        if cookie_name and response.status_code == 200 and "access" in response.data:
            cookie_secure = getattr(settings, "JWT_AUTH_SECURE", False)
            cookie_httponly = getattr(settings, "JWT_AUTH_HTTPONLY", False)
            cookie_samesite = getattr(settings, "JWT_AUTH_SAMESITE", "Lax")

            # read domain from django settings
            cookie_domain = getattr(settings, "SESSION_COOKIE_DOMAIN", None)

            token_expiration = timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME
            response.set_cookie(
                cookie_name,
                response.data["access"],
                expires=token_expiration,
                secure=cookie_secure,
                domain=cookie_domain,
                httponly=cookie_httponly,
                samesite=cookie_samesite,
            )

            response.data["access_token_expiration"] = token_expiration
        return response


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.groups.filter(name__in=settings.STAFF_GROUPS).exists():
            return qs
        return qs.filter(user=self.request.user)


class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsManager]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.groups.filter(name__in=settings.SUPERVISOR_GROUPS).exists():
            return qs
        return qs.exclude(name='Supervisor')


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsManager]


class SetupPasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = SetupPasswordSerializer
    permission_classes = [IsManager]
