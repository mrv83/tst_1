from django.urls import path, include
from .views import Login, RefreshToken, UserView, UserListView, GroupListView, SetupPasswordView

urlpatterns = [
    # path(r'^account/', include('allauth.urls')),
    path("token/refresh/", RefreshToken.as_view(), name="token_refresh"),
    path("login/", Login.as_view()),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path("users/", UserListView.as_view(), name="user_list"),
    path("groups/", GroupListView.as_view(), name="group_list"),
    path("users/<int:pk>/", UserView.as_view(), name="user"),
    path("users/<int:pk>/setup_password/", SetupPasswordView.as_view(), name="setup_password"),
]
