# The Book model has custom permissions: can_view, can_create, can_edit, can_delete

# Groups created: Editors (create/edit), Viewers (view only), Admins (all permissions)

# Use @permission_required decorator in views to enforce these permissions

# settings.py
# Security settings: prevent XSS, clickjacking, enforce HTTPS cookies, and apply CSP headers.

# views.py
# All input is validated using Django forms to prevent SQL injection.
# CSRF tokens are required in all POST forms.
