# LibraryProject (Advanced Features and Security)

**LibraryProject** iis a robust Django web application designed for secure library management. It features custom user models, granular role-based access control (RBAC), and hardened security configurations to protect against common web vulnerabilities.

---

## Key Advanced Features

* Custom User Management: Utilizes a custom user model for flexible authentication.
* Role-Based Access Control (RBAC): Fine-grained permissions (Viewers, Editors, Admins) implemented via custom model permissions.
* Security Hardening:
   -Content Security Policy (CSP): Mitigates XSS by restricting resource loading to trusted sources.

   -HTTPS & HSTS: Enforces secure connections and browser-level SSL persistence.

   -Secure Headers: Implements X-Frame-Options (Anti-Clickjacking) and X-Content-Type-Options.
* Secure CRUD Operations: View, create, and edit books with permission-aware templates and forms.
---

## Technology Used

* **Backend:** Django
* **Database:** SQLite (default with Django)
* **Frontend:** HTML templates (with optional CSS/Bootstrap)

---

## Installation

### Prerequisites

* Python 3.x installed
* Basic knowledge of using the command line

### Steps to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/LibraryProject.git
cd LibraryProject
```````````````````````````

2. **Create a virtual environment**

```bash
python -m venv env
```````````````````````````

3. **Activate the virtual environment**

* On Windows:

```bash
env\Scripts\activate
```````````````````````````

* On Mac/Linux:

```bash
source env/bin/activate
```````````````````````````

4. **Install dependencies**

```bash
pip install -r requirements.txt
```````````````````````````

5. **Apply database migrations**

```bash
python manage.py migrate
```````````````````````````

6. **Create a superuser (admin)**

```bash
python manage.py createsuperuser
```````````````````````````

7. **Run the development server**

```bash
python manage.py runserver
```````````````````````````

8. **Open in your browser**
   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## How to Use

* Visit the home page to see the list of books
* Click on a book to view details
* Borrow or return books (requires login)
* Admin can log in at `/admin` to manage books and members

---

## Security Configuration (Production vs. Development)

The project includes production-ready security settings in settings.py. For local development without SSL, some flags are toggled:

   SSL Redirect: SECURE_SSL_REDIRECT = False (Set to True in production).

   Cookies: CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE are managed based on the environment.

   HSTS: Enabled to ensure long-term secure transport.

## Project Structure

`````````````````````````````````````````````````````````````````````````````````````````````
advanced_features_and_security/
└── LibraryProject/
    ├── bookshelf/             # Core Library App
    │   ├── management/        # Custom commands (setup_groups)
    │   ├── templates/         # Secure, permission-aware templates
    │   ├── models.py          # CustomUser and Book with Permissions
    │   └── forms.py           # Validated forms for safe data entry
    ├── LibraryProject/        # Project settings (Security Middleware/CSP)
    ├── SECURITY.md            # Detailed security implementation report
    └── requirements.txt       # Includes django-csp and other dependencies
`````````````````````````````````````````````````````````````````````````````````````````````

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make changes and commit (`git commit -m "Add feature"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a pull request

---

## License

This project is open source and free to use.

---
