from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from blog_app.models import Post, Comment
from blog_app.forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy




# Create your views here.\
class AboutView(TemplateView):
    template_name = 'blog_app/about.html'


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_list'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_draft_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
