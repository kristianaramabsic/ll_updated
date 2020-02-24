from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from users.models import CustomUser
from django.conf import settings

class ProfileView (DetailView):
    model = CustomUser
    slug_field = 'username'
    template_name = 'user_profile.html'

class UpdateProfileView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    slug_field = 'username'
    template_name = 'edit_profile.html'
    fields = ['photo', 'first_name', 'last_name', 'university', 'department', 'country', 'research_description']
    login_url = 'login'
    
    def test_func(self):
        obj = self.get_object()
        return obj.username == self.request.user.username