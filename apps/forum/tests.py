"""
Tests for the forum app.
"""
from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User

from .models import ForumThread


class ForumTests(TestCase):
    """Test suite for the forum views and permissions."""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all tests."""
        # pylint: disable=no-member
        cls.user = User.objects.create_user(
            username="user",
            email="user@test.com",
            password="pass123",
            is_email_verified=True)
        cls.banned_user = User.objects.create_user(
            username="banned",
            email="banned@test.com",
            password="pass123",
            is_email_verified=True)
        cls.banned_user.is_banned = True
        cls.banned_user.save()
        cls.thread = ForumThread.objects.create(
            title="Test Thread",
            slug="test-thread",
            author=cls.user,
            content="Test content",
        )

    def test_banned_user_cannot_create_thread(self):
        """Ensure a banned user cannot create a forum thread."""
        self.client.login(username="banned", password="pass123")
        response = self.client.post(
            reverse("forum:create-thread"),
            {"title": "Banned thread", "content": "Content"},
        )
        self.assertEqual(response.status_code, 302)
        # pylint: disable=no-member
        self.assertFalse(
            ForumThread.objects.filter(
                title="Banned thread").exists())

    def test_authenticated_user_can_reply(self):
        """Ensure a logged-in user can add a reply."""
        self.client.login(username="user", password="pass123")
        response = self.client.post(
            reverse("forum:add-reply", kwargs={"slug": "test-thread"}),
            {"content": "Test reply"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.thread.replies.count(), 1)

    def test_banned_user_cannot_reply(self):
        """Ensure a banned user cannot add a reply to a thread."""
        self.client.login(username="banned", password="pass123")
        response = self.client.post(
            reverse("forum:add-reply", kwargs={"slug": "test-thread"}),
            {"content": "Banned reply"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.thread.replies.count(), 0)
