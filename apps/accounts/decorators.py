"""
Custom decorators for the accounts app.
"""
from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

def email_verified_required(view_func):
    """
    Decorator for views that checks if the user's email is verified.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('accounts:login')}?next={request.path}")

        if not request.user.is_email_verified:
            messages.warning(request, "Debes verificar tu correo para realizar esta acción.")
            return redirect("accounts:profile")

        return view_func(request, *args, **kwargs)
    return _wrapped_view
