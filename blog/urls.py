from django.urls import path
from .views import HomePageView, AboutPageView, PostPageView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path ('', HomePageView.as_view(), name='homepage'),
    path ('about', AboutPageView.as_view(), name='about'),
    path ('post/<int:pk>/', PostPageView.as_view(), name='post_detail'),
    path ('post/new', BlogCreateView.as_view(), name='post_new'),
    path ('post/<int:pk>/update', BlogUpdateView.as_view(), name='update_post'),
    path ('post/<int:pk>/delete', BlogDeleteView.as_view(), name='delete_post'),
]