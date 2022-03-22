from django.urls import path 
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('article/', views.article,name='blog-article'),
    path('', views.home ,name='blog-home'),
    path('summary/', PostListView.as_view(),name='blog-sumary'),
    path('profile/', views.profile,name='blog-profile'),
    path('home/', views.home,name='blog-home'),
    path('technology/', views.technology,name='blog-tech'),
    path('politics/', views.politics,name='blog-politics'),
    path('entrepreneurship/', views.entrepreneurship,name='blog-entrship'),
]
