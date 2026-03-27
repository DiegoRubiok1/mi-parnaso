from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from apps.accounts.models import User

from .models import Post


class BlogTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.author = User.objects.create_user(username="author", email="author@test.com", password="pass123")
		cls.published_post = Post.objects.create(
			title="Test Post",
			slug="test-post",
			author=cls.author,
			content_md="# Test",
			content_html="<h1>Test</h1>",
			status="published",
			published_at=timezone.now(),
		)
		cls.draft_post = Post.objects.create(
			title="Draft Post",
			slug="draft-post",
			author=cls.author,
			content_md="# Draft",
			content_html="<h1>Draft</h1>",
			status="draft",
		)

	def test_post_list_shows_only_published(self):
		response = self.client.get(reverse("blog:post-list"))
		self.assertContains(response, "Test Post")
		self.assertNotContains(response, "Draft Post")

	def test_post_detail_increments_view_count(self):
		self.assertEqual(self.published_post.view_count, 0)
		self.client.get(reverse("blog:post-detail", kwargs={"slug": "test-post"}))
		self.published_post.refresh_from_db()
		self.assertEqual(self.published_post.view_count, 1)

	def test_comment_requires_login(self):
		response = self.client.post(
			reverse("blog:add-comment", kwargs={"slug": "test-post"}),
			{"content": "Test comment"},
		)
		self.assertEqual(response.status_code, 302)
		self.assertTrue(response.url.startswith("/accounts/login/"))

