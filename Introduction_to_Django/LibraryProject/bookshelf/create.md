# Creating a Book in Django

To add a new book to your Django project, you can use the Django ORM in your views or Django shell.

## Example

```python
from bookshelf.models import Book

# Create a new book instance
book = Book.objects.create(
    title="To Kill a Mockingbird",
    author="Harper Lee",
    published_year=1960
)
```

This will add a new book record to your database.

## Next Steps

- Verify the book was added using the Django admin or shell.
- Customize fields as needed for your project.