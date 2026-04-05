from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from django.db.models import Count

from apps.accounts.decorators import email_verified_required
from .models import ForumReply, ForumThread


class ForumThreadListView(ListView):
	model = ForumThread
	template_name = "forum/thread_list.html"
	context_object_name = "threads"
	paginate_by = 20

	def get_queryset(self):
		return ForumThread.objects.annotate(reply_count_agg=Count('replies')).order_by('-reply_count_agg', '-created_at')


class ForumThreadDetailView(DetailView):
	model = ForumThread
	template_name = "forum/thread_detail.html"
	context_object_name = "thread"
	slug_field = "slug"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		thread = self.get_object()
		context["replies"] = thread.replies.all()
		return context


@email_verified_required
def create_thread_view(request):
	if request.user.is_banned:
		messages.error(request, "No puedes crear temas siendo baneado.")
		return redirect("forum:thread-list")

	if request.method == "POST":
		title = request.POST.get("title", "").strip()
		content = request.POST.get("content", "").strip()
		if title and content:
			if len(title) > 200:
				messages.error(request, "El título del tema no puede tener más de 200 caracteres.")
			else:
				ForumThread.objects.create(title=title, author=request.user, content=content)
				messages.success(request, "Tema creado.")
				return redirect("forum:thread-list")
		else:
			messages.error(request, "Debes llenar todos los campos.")

	return render(request, "forum/create_thread.html")


@email_verified_required
def add_reply_view(request, slug):
	thread = get_object_or_404(ForumThread, slug=slug)

	if request.user.is_banned:
		messages.error(request, "No puedes responder siendo baneado.")
		return redirect("forum:thread-detail", slug=slug)

	if thread.is_locked:
		messages.error(request, "Este tema esta cerrado.")
		return redirect("forum:thread-detail", slug=slug)

	if request.method == "POST":
		content = request.POST.get("content", "").strip()
		if content:
			ForumReply.objects.create(thread=thread, author=request.user, content=content)
			messages.success(request, "Respuesta publicada.")
		return redirect("forum:thread-detail", slug=slug)

	return redirect("forum:thread-detail", slug=slug)
