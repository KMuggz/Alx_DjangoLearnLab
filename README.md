# LibraryProject

**LibraryProject** is a simple Django web application for managing a library.
Users can view books, search for them, borrow and return books, and manage library members.

---

## Features

* View all books in the library
* Search for books by title or author
* Borrow and return books
* Admin panel to add, edit, or remove books and members

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

## Project Structure

`````````````````````````````````````````````````````````````````````````````````````````````
LibraryProject/
│
├── library/           # Main Django app
│   ├── migrations/    # Database migrations
│   ├── templates/     # HTML templates
│   ├── models.py      # Database models
│   ├── views.py       # Logic for web pages
│   └── urls.py        # Routes for app pages
├── LibraryProject/    # Project configuration and settings
├── db.sqlite3         # Default database
├── manage.py          # Django command-line utility
└── requirements.txt   # Python dependencies
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
