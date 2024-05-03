from django.urls import path
from .views import (
    LoginView,
    SignUpView,
    LogOutView,
    ProfilePageView
)
app_name = "users"

urlpatterns = [
    path("users/register/", SignUpView.as_view(), name="register"),
    path("users/login/", LoginView.as_view(), name="login"),
    path("users/profile/", ProfilePageView.as_view(), name="profile"),
    path("users/logout/", LogOutView.as_view(), name="logout"),
    
]
