# Updating a Book in Django

To update a book record in your Django app, follow these steps:

## 1. Create an Update View

```python
from django.views.generic.edit import UpdateView
from .models import Book

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'bookshelf/book_form.html'
    success_url = '/books/'
```

## 2. Add URL Pattern

```python
from django.urls import path
from .views import BookUpdateView

urlpatterns = [
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-update'),
]
```

## 3. Create/Edit the Template

Create or update `bookshelf/templates/bookshelf/book_form.html`:

```django
<h2>Update Book</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Save Changes</button>
</form>
```

## 4. Usage

Visit `/books/<book_id>/edit/` to update a book.
