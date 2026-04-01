"""
URL configuration for the accounts app.
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import profile_view, register_view, send_verification_email, verify_email

APP_NAME = "accounts"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
    path("verify-email/send/", send_verification_email, name="send-verification-email"),
    path("verify/<str:uidb64>/<str:token>/", verify_email, name="verify-email"),
]
