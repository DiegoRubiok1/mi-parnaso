"""
Tests for the accounts app.
"""
from django.test import TestCase
from django.urls import reverse

from .models import User


class AccountsTests(TestCase):
    """
    Test cases for the accounts application.
    """
    def test_register_creates_profile(self):
        """
        Test that registering a user automatically creates a profile.
        """
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "ana",
                "email": "ana@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username="ana")
        self.assertTrue(hasattr(user, "profile"))

    def test_duplicate_email_is_rejected(self):
        """
        Test that registering with a duplicate email is rejected.
        """
        User.objects.create_user(username="u1", email="x@example.com", password="StrongPass123!")
        response = self.client.post(
            reverse("accounts:register"),
            {
                "username": "u2",
                "email": "x@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este email ya esta en uso.")

    def test_logout_with_post_works(self):
        """
        Test that logging out via POST works correctly.
        """
        user = User.objects.create_user(
            username="ana2", email="ana2@example.com", password="StrongPass123!"
        )
        self.client.force_login(user)

        response = self.client.post(reverse("accounts:logout"), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout_with_get_is_not_allowed(self):
        """
        Test that logging out via GET is not allowed.
        """
        user = User.objects.create_user(
            username="ana3", email="ana3@example.com", password="StrongPass123!"
        )
        self.client.force_login(user)

        response = self.client.get(reverse("accounts:logout"))

        self.assertEqual(response.status_code, 405)
