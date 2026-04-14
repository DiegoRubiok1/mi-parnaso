"""
Views for the blog application.
"""
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from apps.accounts.decorators import email_verified_required
from .models import Post, PostComment, Tag


class PostListView(ListView):
    """View to list all published blog posts."""
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        # pylint: disable=no-member
        qs = Post.objects.filter(status="published").order_by("-published_at")
        tag_slug = self.request.GET.get("tag")
        if tag_slug:
            qs = qs.filter(tags__slug=tag_slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pylint: disable=no-member
        context["tags"] = Tag.objects.all()
        context["current_tag"] = self.request.GET.get("tag")
        return context


class PostDetailView(DetailView):
    """View to display details of a single post."""
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_field = "slug"

    def get_queryset(self):
        # pylint: disable=no-member
        return Post.objects.filter(status="published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context[self.context_object_name]
        context["comments"] = post.comments.all()
        return context

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        # Check if the post has already been viewed in the current session
        viewed_posts = self.request.session.get('viewed_posts', [])
        if obj.id not in viewed_posts:
            obj.view_count += 1
            obj.save(update_fields=["view_count"])
            viewed_posts.append(obj.id)
            self.request.session['viewed_posts'] = viewed_posts
            
        return obj


@email_verified_required
def add_comment_view(request, slug):
    """Handle adding a new comment to a post."""
    # pylint: disable=no-member
    post = get_object_or_404(Post, slug=slug, status="published")
    if request.method == "POST":
        content = request.POST.get("content", "").strip()
        if content:
            PostComment.objects.create(
                post=post, author=request.user, content=content)
            messages.success(request, "Comentario publicado.")
        return redirect("blog:post-detail", slug=slug)
    return redirect("blog:post-detail", slug=slug)
