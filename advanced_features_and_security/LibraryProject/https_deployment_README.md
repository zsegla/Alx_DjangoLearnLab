# HTTPS and Secure Redirects in Django

## Django Settings for HTTPS

- `SECURE_SSL_REDIRECT = True` # Redirect all HTTP requests to HTTPS
- `SECURE_HSTS_SECONDS = 31536000` # Enforce HTTPS for 1 year
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True` # Apply HSTS to all subdomains
- `SECURE_HSTS_PRELOAD = True` # Allow site to be included in browser preload lists
- `SESSION_COOKIE_SECURE = True` # Session cookies only sent over HTTPS
- `CSRF_COOKIE_SECURE = True` # CSRF cookies only sent over HTTPS
- `X_FRAME_OPTIONS = 'DENY'` # Prevent clickjacking
- `SECURE_CONTENT_TYPE_NOSNIFF = True` # Prevent MIME sniffing
- `SECURE_BROWSER_XSS_FILTER = True` # Enable browser XSS filter

## Deployment Configuration

1. **Obtain SSL/TLS Certificates**
   - Use Let's Encrypt, your hosting provider, or a commercial CA.
2. **Web Server Setup**
   - For Nginx, add:
     ```
     server {
         listen 443 ssl;
         server_name yourdomain.com;
         ssl_certificate /path/to/fullchain.pem;
         ssl_certificate_key /path/to/privkey.pem;
         ...
     }
     ```
   - For Apache, add:
     ```
     <VirtualHost *:443>
         ServerName yourdomain.com
         SSLEngine on
         SSLCertificateFile /path/to/cert.pem
         SSLCertificateKeyFile /path/to/privkey.pem
         ...
     </VirtualHost>
     ```
3. **Redirect HTTP to HTTPS**
   - Nginx:
     ```
     server {
         listen 80;
         server_name yourdomain.com;
         return 301 https://$host$request_uri;
     }
     ```
   - Apache:
     ```
     <VirtualHost *:80>
         ServerName yourdomain.com
         Redirect permanent / https://yourdomain.com/
     </VirtualHost>
     ```

## Security Review

- All cookies are secure and only sent over HTTPS.
- All HTTP requests are redirected to HTTPS.
- HSTS is enabled for 1 year and includes subdomains and preload.
- Clickjacking, XSS, and MIME sniffing protections are enabled.
- Review and test your deployment with SSL Labs and securityheaders.com.
