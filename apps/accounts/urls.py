"""
URL configuration for the accounts app.
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from .forms import CustomPasswordResetForm
from .views import (
    profile_view,
    register_view,
    send_verification_email,
    toggle_subscription,
    verify_email,
)

app_name = "accounts"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
    path("verify-email/send/", send_verification_email, name="send-verification-email"),
    path("verify/<str:uidb64>/<str:token>/", verify_email, name="verify-email"),
    path(
        "toggle-subscription/<str:subscription_type>/",
        toggle_subscription,
        name="toggle-subscription",
    ),
    # Password Reset
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            form_class=CustomPasswordResetForm,
            template_name="accounts/password_reset_form.html",
            email_template_name="accounts/password_reset_email.html",
            subject_template_name="accounts/password_reset_subject.txt",
            success_url="/accounts/password-reset/done/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url="/accounts/password-reset-complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
