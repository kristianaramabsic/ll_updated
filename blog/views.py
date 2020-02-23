from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.conf import settings

class HomePageView (ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'

class AboutPageView (TemplateView):
    template_name = 'about.html'

class PostPageView (DetailView):
    model = Post
    template_name = 'posts.html'

class BlogCreateView (LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'text']
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'text']
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('homepage')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user