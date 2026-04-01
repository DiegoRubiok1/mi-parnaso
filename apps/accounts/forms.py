"""
Forms for the accounts app.
"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from .models import Profile

User = get_user_model()


class RegisterForm(UserCreationForm):
    """
    Form for user registration.
    """
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):  # pylint: disable=too-many-ancestors
        """
        Meta options for RegisterForm.
        """
        model = User
        fields = ("username", "email", "password1", "password2")

    # pylint: disable=too-few-public-methods

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Nombre de usuario"
        self.fields["username"].help_text = "Solo letras, numeros y @/./+/-/_"
        self.fields["username"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Ej: lector_urbano",
                "autocomplete": "username",
            }
        )

        self.fields["email"].label = "Email"
        self.fields["email"].help_text = "Usaremos este correo para tu acceso."
        self.fields["email"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "tu@email.com",
                "autocomplete": "email",
            }
        )

        self.fields["password1"].label = "Contraseña"
        self.fields["password1"].help_text = ""
        self.fields["password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Minimo 8 caracteres",
                "autocomplete": "new-password",
            }
        )

        self.fields["password2"].label = "Repetir contraseña"
        self.fields["password2"].help_text = ""
        self.fields["password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Repite la contraseña",
                "autocomplete": "new-password",
            }
        )

    def clean_email(self):
        """
        Validate that the email is unique.
        """
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya esta en uso.")
        return email


class ProfileForm(forms.ModelForm):
    """
    Form for updating user profile.
    """
    class Meta:  # pylint: disable=too-few-public-methods
        """
        Meta options for ProfileForm.
        """
        model = Profile
        fields = ("photo", "bio")
