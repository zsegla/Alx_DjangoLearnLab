from relationship_app.models import Author, Book, Library, Librarian

def books_by_author(author_name):
    """Query all books by a specific author name."""
    try:
        author = Author.objects.get(name=author_name)
        return list(Book.objects.filter(author=author))
    except Author.DoesNotExist:
        return []

def books_in_library(library_name):
    """List all books in a library by library name."""
    try:
        library = Library.objects.get(name=library_name)
        return list(library.books.all())
    except Library.DoesNotExist:
        return []

def librarian_for_library(library_name):
    """Retrieve the librarian for a library by library name."""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage (for Django shell or script run with Django context):
if __name__ == "__main__":
    # Replace with actual names in your DB
    print("Books by Author:", books_by_author("Author Name"))
    print("Books in Library:", books_in_library("Library Name"))
    print("Librarian for Library:", librarian_for_library("Library Name"))
