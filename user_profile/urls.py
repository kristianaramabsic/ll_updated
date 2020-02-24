from django.urls import path
from .views import ProfileView, UpdateProfileView

app_name = 'user_profile'
urlpatterns = [
    path('<str:slug>', ProfileView.as_view(), name='user_profile'),
    path('<str:slug>/edit', UpdateProfileView.as_view(), name='edit_profile'),
]