from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from django.urls import reverse
from typing import cast

class BookAPITestCase(APITestCase):
    # comprehensive test suite for the Book API endpoints

    def setUp(self):
        # create a user for authentification tests
        self.user = User.objects.create_user(
            username='testuser', 
            password='password123'
        )
        self.client = APIClient()

        # create initial data
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author            
        )

        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk':self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk':self.book.pk})

# ---CRUD TESTS---

    def test_create_book_authenticator(self):
        # test that the authenticated user can create a book
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "The Hobbit",
            "publication_year": 1937,
            "author": self.author.pk
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unautheticated(self):
        # test that an unauthenticated user can't create a book
        data = {
            "title": "Forbidden Book", 
            "publication_year": 2020, 
            "author": self.author.pk
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_books(self):
        # test retrieving the list of books (public acccess)
        response = cast(Response, self.client.get(self.list_url))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)
        data = cast(list, response.data)
        self.assertEqual(len(data), 1)

    def test_update_book(self):
        # test updating a book's title
        self.client.login(username='testuser', password='password123')
        data = {
            "title": "Harry Potter and the Chamber of Secrets", 
            "publication_year": 1998, 
            "author": self.author.pk
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Chamber of Secrets")

    def test_delete_book(self):
        # test deleting a book
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

# ---filtering & searching tests---

    def test_filter_books_by_year(self):
        # tst filtering books by publication year
        response = cast(Response, self.client.get(f'{self.list_url}?publication_year=1997'))
        self.assertIsNotNone(response.data)
        data = cast(list, response.data)
        self.assertEqual(len(data), 1)
        
        response = cast(Response, self.client.get(f'{self.list_url}?publication_year=2000'))
        self.assertIsNotNone(response.data)
        data = cast(list, response.data)
        self.assertEqual(len(data), 0)

    def test_search_books_by_title(self):
        # test searching for a book by the title keyword
        response = cast(Response, self.client.get(f'{self.list_url}?search=Harry'))
        data = cast(list, response.data)
        self.assertEqual(len(data), 1)

# ---custom validation test---
    def test_validation_future_year(self):
        # test that the serializer prevents future publication years (testing future dates)
        self.client.login(username='testuser', password='password123')
        future_year = 2050
        data = {
            "title": "Future Book", 
            "publication_year": future_year, 
            "author": self.author.pk
        }
        response = cast(Response, self.client.post(self.create_url, data))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsNotNone(response.data)
        data = cast(dict, response.data)
        self.assertIn("publication_year", data)

