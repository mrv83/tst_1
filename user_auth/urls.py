from django.urls import path, include
from .views import Login, RefreshToken


urlpatterns = [
    # path(r'^account/', include('allauth.urls')),
    path("token/refresh/", RefreshToken.as_view(), name="token_refresh"),
    path("login/", Login.as_view()),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
]