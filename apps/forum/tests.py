from django.test import TestCase
from django.urls import reverse

from apps.accounts.models import User

from .models import ForumThread


class ForumTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="user", email="user@test.com", password="pass123")
        cls.banned_user = User.objects.create_user(username="banned", email="banned@test.com", password="pass123")
        cls.banned_user.is_banned = True
        cls.banned_user.save()
        cls.thread = ForumThread.objects.create(
            title="Test Thread",
            slug="test-thread",
            author=cls.user,
            content="Test content",
        )

    def test_banned_user_cannot_create_thread(self):
        self.client.login(username="banned", password="pass123")
        response = self.client.post(
            reverse("forum:create-thread"),
            {"title": "Banned thread", "content": "Content"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(ForumThread.objects.filter(title="Banned thread").exists())

    def test_authenticated_user_can_reply(self):
        self.client.login(username="user", password="pass123")
        response = self.client.post(
            reverse("forum:add-reply", kwargs={"slug": "test-thread"}),
            {"content": "Test reply"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.thread.replies.count(), 1)

    def test_banned_user_cannot_reply(self):
        self.client.login(username="banned", password="pass123")
        response = self.client.post(
            reverse("forum:add-reply", kwargs={"slug": "test-thread"}),
            {"content": "Banned reply"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.thread.replies.count(), 0)
