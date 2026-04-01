from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import ProfileForm, RegisterForm

User = get_user_model()


def register_view(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect("core:home")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


@login_required
def send_verification_email(request):
    """Verification email view"""

    if request.user.is_email_verified:
        messages.info(request, "Tu correo ya está verificado.")
        return redirect("accounts:profile")

    user = request.user
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
	domain = request.get_host()
	link = f"http://{domain}/accounts/verify/{uid}/{token}/"

    subject = "Verifica tu correo electrónico - Mi Parnaso"
    message = f"Hola {user.username},\n\nPor favor, verifica tu correo haciendo clic en el siguiente enlace:\n{link}"

    # En un entorno real, usarías render_to_string para un email HTML
    try:
        send_mail(subject, message, None, [user.email])
        messages.success(request, "Se ha enviado un correo de verificación.")
    except Exception:
        messages.error(request, "Hubo un error al enviar el correo. Inténtalo más tarde.")

    return redirect("accounts:profile")


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.success(request, "¡Tu correo ha sido verificado correctamente!")
        if not request.user.is_authenticated:
            login(request, user)
        return redirect("core:home")
    else:
        messages.error(request, "El enlace de verificación es inválido o ha expirado.")
        return redirect("core:home")


@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/profile.html", {"form": form})
