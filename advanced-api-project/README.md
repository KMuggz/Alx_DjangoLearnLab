# Advanced API Project: Book Management System

This project is a robust Django-based API for managing an inventory of authors and books. It demonstrates advanced concepts in Django REST Framework (DRF), including nested serialization, custom data validation, and granular permission controls.

## Features

    Nested Relationships: Authors include a list of their related books in their API response.

    Custom Validation: Books cannot be saved with a publication year set in the future.

    Granular Permissions: Public read-only access with restricted write access for authenticated users.

    Advanced Querying: Users can filter, search, and sort the book collection via URL parameters.

## API Documentation
Base URL

`/api/`

**Endpoints**

| Endpoint | Method | Description | Permissions |
|:---------|:--------:|:-------------:|-------------:|
| `books/` | GET | List all available books. | Public |
| `books/<int:pk>/` | GET | Retrieve detailed info of a specific book. | Public |
| `books/create/` | POST | Add a new book to the database. | Authenticated |
| `books/update/<int:pk>/` | PUT / PATCH | Update details of an existing book. | Authenticated |
| `books/delete/<int:pk>/` | DELETE | Remove a book from the database. | Authenticated |

**Query Parameters (for books/)**

| Parameter | Type | Description | Example|
|:---------|:--------:|:-------------:|-------------:|
| `title` | Filter | Exact match for book title. | `?title=1984` |
| `author` | Filter | Exact match for author ID. | `?author=1` |
| `publication_year` | Filter | Exact match for year. | `?publication_year=1949` |
| `search` | Search | Partial match in title or author name. | `?search=George` |
| `ordering` | Order | Sort by title or publication year (use `-` for descending). | `?ordering=-publication_year` |

## View Configuration Details

All views for the Book model are built using Django REST Framework Generic Views found in api/views.py.
1. **BookListView & BookDetailView**
~~~
    Class: ListAPIView and RetrieveAPIView.

    Purpose: Provide read-only access to the book collection.

    Advanced Querying: BookListView supports DjangoFilterBackend, SearchFilter, and OrderingFilter.

    Permission: IsAuthenticatedOrReadOnly. This ensures that unauthenticated users can still consume the API data without modifying it.
~~~


2. **BookCreateView**
~~~

    Class: CreateAPIView.

    Custom Behavior: Uses the BookSerializer which includes a custom validate_publication_year hook to prevent future-dated entries.

    Permission: IsAuthenticated. Only registered users can contribute new books.
~~~

3. **BookUpdateView**
~~~

    Class: UpdateAPIView.

    Purpose: Allows for both full (PUT) and partial (PATCH) updates to book records.

    Permission: IsAuthenticated.
~~~

4. **BookDeleteView**
~~~

    Class: DestroyAPIView.

    Purpose: Handles the safe removal of book instances by their primary key.

    Permission: IsAuthenticated.
~~~

## Testing
    The integrity of this API is maintained through a comprehensive suite of unit tests located in api/test_views.py. These tests utilize Django's APITestCase and the reverse utility for dynamic URL resolution.

    Coverage Areas:

    >CRUD Operations: Verifies successful creation, retrieval, modification, and deletion of records.

    >Permissions: Ensures that data modification is restricted to authenticated users.

    >Advanced Querying: Validates that filtering, searching, and ordering return accurate data subsets.

    >Custom Validation: Confirms that the API rejects invalid publication years.

    **Running the Tests:**

    ~~~To execute the test suite, run the following command in your terminal:~~~

    *python manage.py test __api__*


## Installation & Setup

    Clone the repository.

    Install dependencies: pip install django djangorestframework django-filter.

    Run migrations: python manage.py migrate.

    Start the server: python manage.py runserver.