from django.test import TestCase
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorBookSerializerTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author)

    def test_book_serializer_valid(self):
        serializer = BookSerializer(self.book1)
        self.assertEqual(serializer.data['title'], "Book One")
        self.assertEqual(serializer.data['publication_year'], 2020)

    def test_book_serializer_invalid_year(self):
        from datetime import datetime
        future_year = datetime.now().year + 1
        data = {"title": "Future Book", "publication_year": future_year, "author": self.author.id}
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('publication_year', serializer.errors)

    def test_author_serializer_nested_books(self):
        serializer = AuthorSerializer(self.author)
        self.assertEqual(len(serializer.data['books']), 2)
        self.assertEqual(serializer.data['books'][0]['title'], "Book One")
        self.assertEqual(serializer.data['books'][1]['title'], "Book Two")
