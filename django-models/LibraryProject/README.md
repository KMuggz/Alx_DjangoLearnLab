# LibraryProject-(relationship_app addition)

**Advanced Library Management System**
An advanced Django-based library management system featuring complex data relationships, custom user roles, and fine-grained permission controls. It builds on the Introduction_to_Django project by using a relationship_app.

---

## Features

* Custom RBAC (Role-Based Access Control): Implemented distinct user roles (Admin, Librarian, Member) using a UserProfile model and Django signals for automatic profile creation.
* Granular Permissions: Defined custom model permissions (can_add_book, can_change_book, can_delete_book) and secured views using the @permission_required decorator.
* Hybrid View Architecture: Balanced the use of Function-Based Views (FBVs) for custom logic and Class-Based Views (CBVs) for standard object details.
* Production-Ready Database: Migrated from default SQLite to a robust MySQL backend, managing environment variables with python-dotenv.
* Secure Authentication: Implemented a full auth flow including registration, login, and secure logout (using POST requests as per Django 6.0 standards).

---

## Technology Used

* **Backend:** Django 6.0.1
* **Database:** SQLite (default with Django) (I used MySQL 🐬)
* **Environment Management:** python-dotenv
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

2.**Create a virtual environment**

```bash
python -m venv .venv
```````````````````````````

3.**Activate the virtual environment**

* On Windows:

```bash
.venv\Scripts\activate
```````````````````````````

* On Mac/Linux:

```bash
source .venv/bin/activate
```````````````````````````

4.**Install dependencies**

```bash
pip install -r requirements.txt
```````````````````````````

5.**Apply database migrations**

```bash
python manage.py migrate
```````````````````````````

6.**Create a superuser (admin)**

```bash
python manage.py createsuperuser
```````````````````````````

7.**Run the development server**

```bash
python manage.py runserver
```````````````````````````

8.**Open in your browser**
   Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## How to Use

* Visit the home page to see the list of books
* Click on a book to view details
* Borrow or return books (requires login)
* Admin can log in at `/admin` to manage books and members

---

## Project Structure

`````````````````````````````````````````````````````````````````````````````````````````````
LibraryProject/
├── relationship_app/        # Core logic app
│   ├── models.py            # RBAC & Book relationships
│   ├── signals.py           # Auto-profile generation
│   ├── query_samples.py     # ORM performance testing
│   ├── templates/           # Namespaced HTML templates
│   └── views.py             # Role-protected view logic
├── LibraryProject/          # Main settings & URL routing
└── manage.py                # Django Command Line Interface
`````````````````````````````````````````````````````````````````````````````````````````````

---

## Testing the Roles

   Admin: Full access to the /admin/ dashboard and admin_view.

   Librarian: Access to librarian_view and book management (add/edit).

   Member: Access to member_view and standard book listing.

---

## Lessons Learned

During this project, I navigated the complexities of manual path resolution in the Django shell, handled CSRF (Cross-Site Request Forgery) security requirements for authentication, and mastered the logic of decorators to protect sensitive views.

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
