from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,PostByTagListView
)
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
from .views import search_posts, posts_by_tag

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('posts/', PostListView.as_view(), name='post_list'),  # list view can stay plural
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # singular 'post/new/'
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # singular 'update'
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # singular 'delete'
    
    
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),

    # Update a comment by comment ID
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),

    # Delete a comment by comment ID
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag'),
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),


]
