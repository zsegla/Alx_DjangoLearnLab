Contents (short):

What it does: Registration (username + email + password), login/logout (Django built-in views), profile editing (bio/avatar).

Files to look at:

blog/forms.py: UserRegisterForm, UserUpdateForm, ProfileUpdateForm

blog/views.py: register, profile

blog/models.py: Profile (OneToOne)

blog/urls.py: register, login, logout, profile

Templates: blog/templates/blog/\*.html

How to test:

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Register at /register/, log in at /login/, edit at /profile/.

Deployment notes:

Configure media (serve via cloud storage or via proper server when DEBUG=False).

Enforce HTTPS, secure cookies, set CSRF_TRUSTED_ORIGINS if needed.

To add: email verification, password reset (Django has PasswordResetView etc.), social auth (django-allauth)

Access control: Only authenticated users can create posts; only the author can edit/delete.

Navigation: List → Detail → Create/Edit/Delete.

URLs: /posts/, /posts/new/, /posts/<pk>/, /posts/<pk>/edit/, /posts/<pk>/delete/.

Include this explanation in your README or as code comments.

Add Comment: /posts/<post_id>/comments/new/ → POST by authenticated users.

Edit Comment: /comments/<comment_id>/edit/ → Only author can edit.

Delete Comment: /comments/<comment_id>/delete/ → Only author can delete.

Permissions: Checked via login_required and filtering by author=request.user.

Tagging and Search Features – Quick Guide

1. Tagging Posts

Posts can have multiple tags (many-to-many).

Tags are displayed on the post detail page.

Clicking a tag shows all posts with that tag (/tags/<tag_name>/).

2. Search Functionality

Search bar is in the header (base.html).

Users can search posts by title, content, or tag names.

Search results are shown on a dedicated page (/search/).

3. URLs

path('tags/<str:tag_name>/', views.posts_by_tag, name='posts_by_tag')

path('search/', views.search_posts, name='search_posts')

4. Templates

posts_by_tag.html – lists posts for a tag.

search_results.html – displays posts matching a search query.

post_detail.html – displays tags and comments for a post.

5. Views

posts_by_tag(request, tag_name) – filters posts by tag.

search_posts(request) – filters posts by search query using Q lookups.