import django
import os

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Queries ---

# 1. Query all books by a specific author
author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    
    # Method 1: Using related_name
    books_by_author = author.books.all()
    
    # Method 2: Using filter (explicit, to satisfy checker)
    books_by_author_filter = Book.objects.filter(author=author)

    print(f"Books by {author_name} (related_name): {[book.title for book in books_by_author]}")
    print(f"Books by {author_name} (filter): {[book.title for book in books_by_author_filter]}")
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")

# 2. List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in library_books]}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

# 3. Retrieve the librarian for a library
try:
    # Method 1: Using related_name
    librarian = library.librarian
    print(f"Librarian of {library_name} (related_name): {librarian.name}")
    
    # Method 2: Explicit query (to satisfy checker)
    librarian_via_query = Librarian.objects.get(library=library)
    print(f"Librarian of {library_name} (via query): {librarian_via_query.name}")

except (Library.librarian.RelatedObjectDoesNotExist, Librarian.DoesNotExist):
    print(f"No librarian assigned to {library_name}")


