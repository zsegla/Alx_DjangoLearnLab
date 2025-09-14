from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

# After deleting the book, you can verify the deletion by checking the list of books:

for book in Book.objects.all():
    print(book.title)