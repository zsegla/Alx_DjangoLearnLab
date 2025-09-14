# Django Security Best Practices Implemented

## settings.py

- `DEBUG = False` for production.
- `SECURE_BROWSER_XSS_FILTER = True` to enable browser XSS filter.
- `X_FRAME_OPTIONS = 'DENY'` to prevent clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` to prevent MIME sniffing.
- `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` to ensure cookies are sent over HTTPS only.
- (Optional) Content Security Policy (CSP) middleware and settings are commented for use with `django-csp`.

## Templates

- All forms include `{% csrf_token %}` for CSRF protection.
- Book form uses Django's form rendering to ensure safe input handling.

## Views

- All user input is validated using Django forms (`BookForm`).
- No raw SQL is used; all queries use Django ORM.

## Testing

- Manually test forms and input fields for CSRF and XSS vulnerabilities.
- Ensure only authorized users can access protected views.

## Notes

- For full CSP support, install and configure `django-csp`.
- Always review and update `ALLOWED_HOSTS` and other settings for your deployment environment.
