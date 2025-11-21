Security Review – HTTPS & Secure Redirects

This project implements full HTTPS enforcement using Django security settings and server-level SSL configuration.

🔐 Django Security Settings Added

SECURE_SSL_REDIRECT: forces all HTTP requests to use HTTPS

SECURE_HSTS_SECONDS, SECURE_HSTS_PRELOAD: enforce browser-level HTTPS

SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE: cookies only sent over HTTPS

X_FRAME_OPTIONS = "DENY": prevents clickjacking

SECURE_CONTENT_TYPE_NOSNIFF: prevents MIME sniffing

SECURE_BROWSER_XSS_FILTER: enables browser XSS protection

🔏 Deployment Security

Configured server to:

Serve SSL certificates

Redirect HTTP → HTTPS

Proxy Django through HTTPS

✔ Benefits

Prevents man-in-the-middle attacks

Protects session cookies

Prevents most common XSS & clickjacking attacks

Ensures browser enforces HTTPS

❗ Areas to Improve Later

Add CSP headers for advanced XSS protection

Implement rate limiting

Use HTTPS-only third-party libraries