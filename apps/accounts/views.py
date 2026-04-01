"""
Views for the accounts app.
"""
import logging

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import ProfileForm, RegisterForm

User = get_user_model()
logger = logging.getLogger(__name__)


def register_view(request):
    """
    View for user registration.
    """
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
    """
    Verification email view to send a verification link to the user.
    """

    if request.user.is_email_verified:
        messages.info(request, "Tu correo ya está verificado.")
        return redirect("accounts:profile")

    user = request.user
    if not user.email:
        messages.error(request, "Tu usuario no tiene correo configurado.")
        return redirect("accounts:profile")

    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verify_path = reverse("accounts:verify-email", kwargs={"uidb64": uid, "token": token})
    if settings.SITE_URL:
        link = f"{settings.SITE_URL.rstrip('/')}{verify_path}"
    else:
        link = request.build_absolute_uri(verify_path)

    subject = "Verifica tu correo electrónico - Mi Parnaso"
    message = (
        f"Hola {user.username},\n\n"
        f"Por favor, verifica tu correo haciendo clic en el siguiente enlace:\n{link}"
    )

    try:
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
        messages.success(request, "Se ha enviado un correo de verificación.")
    except Exception:  # pylint: disable=broad-exception-caught
        logger.exception("Error enviando correo de verificacion a %s", user.email)
        messages.error(request, "Hubo un error al enviar el correo. Inténtalo más tarde.")

    return redirect("accounts:profile")


def verify_email(request, uidb64, token):
    """
    View to verify the user's email using the link sent via email.
    """
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

    messages.error(request, "El enlace de verificación es inválido o ha expirado.")
    return redirect("core:home")


@login_required
def profile_view(request):
    """
    View for displaying and updating the user profile.
    """
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


@login_required
def toggle_subscription(request, subscription_type):
    """
    Toggle user subscription to blog or forum.
    """
    if not request.user.is_email_verified:
        messages.error(
            request, "Debes verificar tu correo electrónico para suscribirte a las notificaciones."
        )
        if request.headers.get("HX-Request"):
            return render(
                request,
                "accounts/partials/subscription_buttons.html",
                {"profile": request.user.profile, "user": request.user},
            )
        return redirect("accounts:profile")

    profile = request.user.profile
    if subscription_type == "blog":
        profile.subscribe_to_blog = not profile.subscribe_to_blog
    elif subscription_type == "forum":
        profile.subscribe_to_forum = not profile.subscribe_to_forum
    profile.save()

    if request.headers.get("HX-Request"):
        return render(
            request,
            "accounts/partials/subscription_buttons.html",
            {"profile": profile, "user": request.user},
        )

    return redirect("blog:post-list")
