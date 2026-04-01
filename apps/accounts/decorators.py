from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

def email_verified_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"{reverse('accounts:login')}?next={request.path}")
        
        if not request.user.is_email_verified:
            messages.warning(request, "Debes verificar tu correo electrónico para realizar esta acción.")
            return redirect("accounts:profile") # O a una página específica de verificación
            
        return view_func(request, *args, **kwargs)
    return _wrapped_view
