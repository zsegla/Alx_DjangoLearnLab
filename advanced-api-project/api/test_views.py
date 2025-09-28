from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()

        # Create test authors
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        # Create test books
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author2)

    def authenticate(self):
        """Helper method to login"""
        self.client.login(username="testuser", password="testpass")

    # ------------------------------
    # LIST and DETAIL
    # ------------------------------
    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Book One")

    # ------------------------------
    # CREATE
    # ------------------------------
    def test_create_book_authenticated(self):
        self.authenticate()
        url = reverse("book-create")
        data = {
            "title": "Book Three",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "Book Three")

    def test_create_book_unauthenticated(self):
        url = reverse("book-create")
        data = {
            "title": "Book Three",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------------------
    # UPDATE
    # ------------------------------
    def test_update_book_authenticated(self):
        self.authenticate()
        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Book One Updated",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Book One Updated")

    def test_update_book_unauthenticated(self):
        url = reverse("book-update", args=[self.book1.id])
        data = {
            "title": "Book One Updated",
            "publication_year": 2022,
            "author": self.author1.id
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------------------
    # DELETE
    # ------------------------------
    def test_delete_book_authenticated(self):
        self.authenticate()
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_book_unauthenticated(self):
        url = reverse("book-delete", args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------------------
    # FILTERING / SEARCH / ORDERING (Optional but recommended)
    # ------------------------------
    def test_filter_books_by_author(self):
        url = reverse("book-list") + "?author__name=Author One"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], self.author1.id)

    def test_search_books_by_title(self):
        url = reverse("book-list") + "?search=Book Two"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book Two")

    def test_order_books_by_publication_year(self):
        url = reverse("book-list") + "?ordering=-publication_year"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 2021)
