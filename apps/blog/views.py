from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView

from .models import Post, PostComment, Tag


class PostListView(ListView):
	model = Post
	template_name = "blog/post_list.html"
	context_object_name = "posts"
	paginate_by = 10

	def get_queryset(self):
		qs = Post.objects.filter(status="published").order_by("-published_at")
		tag_slug = self.request.GET.get("tag")
		if tag_slug:
			qs = qs.filter(tags__slug=tag_slug)
		return qs

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["tags"] = Tag.objects.all()
		context["current_tag"] = self.request.GET.get("tag")
		return context


class PostDetailView(DetailView):
	model = Post
	template_name = "blog/post_detail.html"
	context_object_name = "post"
	slug_field = "slug"

	def get_queryset(self):
		return Post.objects.filter(status="published")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		post = context[self.context_object_name]
		context["comments"] = post.comments.all()
		return context

	def get_object(self, queryset=None):
		obj = super().get_object(queryset)
		obj.view_count += 1
		obj.save(update_fields=["view_count"])
		return obj


@login_required
def add_comment_view(request, slug):
	post = get_object_or_404(Post, slug=slug, status="published")
	if request.method == "POST":
		content = request.POST.get("content", "").strip()
		if content:
			PostComment.objects.create(post=post, author=request.user, content=content)
			messages.success(request, "Comentario publicado.")
		return redirect("blog:post-detail", slug=slug)
	return redirect("blog:post-detail", slug=slug)
