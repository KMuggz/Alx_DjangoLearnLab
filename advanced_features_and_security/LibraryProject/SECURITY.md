# Security Policy: Advanced Library Management System

This document outlines the security measures implemented in the LibraryProject to protect user data and ensure system integrity.

## 1. Authentication and Access Control
- **Custom User Model**: Implemented a `CustomUser` model to handle unique identifiers and additional profile data securely.
- **Granular Permissions**: Defined custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) within the `Book` model to enforce the Principle of Least Privilege.
- **Role-Based Access Control (RBAC)**: Created automated groups (Admins, Editors, Viewers) with specific permission sets.
- **View Protection**: All sensitive views are protected by the `@permission_required` decorator, ensuring unauthorized users cannot access or modify data.

## 2. Protection Against Common Vulnerabilities
- **Cross-Site Scripting (XSS)**:
  - Enabled `SECURE_BROWSER_XSS_FILTER`.
  - Implemented a strict **Content Security Policy (CSP)** to restrict script execution to trusted sources.
  - Utilized Django's auto-escaping template engine.
- **Cross-Site Request Forgery (CSRF)**:
  - Enforced `{% csrf_token %}` on all state-changing (POST) forms.
  - Configured `CSRF_COOKIE_SECURE` for encrypted transmission.
- **Clickjacking**:
  - Set `X_FRAME_OPTIONS = 'DENY'` to prevent the site from being rendered inside malicious iframes.
- **SQL Injection**:
  - Used Django ORM and `ModelForm` for all database interactions to ensure query parameterization.

## 3. Secure Communication
- **HTTPS Enforcement**: Configured `SECURE_SSL_REDIRECT` to upgrade all HTTP requests to HTTPS.
- **HSTS (HTTP Strict Transport Security)**: Activated `SECURE_HSTS_SECONDS` (1 year) with subdomains and preloading to ensure browsers never fallback to insecure connections.
- **Cookie Security**: Set `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` to ensure tokens are never sent over unencrypted channels.

## 4. Browser Hardening
- **MIME Sniffing**: Enabled `SECURE_CONTENT_TYPE_NOSNIFF` to prevent browsers from executing non-executable files as scripts.