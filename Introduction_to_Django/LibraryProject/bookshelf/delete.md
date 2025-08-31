# Deleting a Book in Django

To delete a book from your Django application, follow these steps:

## 1. Update `views.py`

```python
from django.shortcuts import get_object_or_404, redirect
from .models import Book

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})
```

## 2. Add URL Pattern

In `urls.py`:

```python
from . import views

urlpatterns = [
    # ... other patterns ...
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
```

## 3. Create a Confirmation Template

Create `delete_book.html`:

```html
<h2>Delete Book</h2>
<p>Are you sure you want to delete "{{ book.title }}"?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit">Confirm Delete</button>
    <a href="{% url 'book_list' %}">Cancel</a>
</form>
```

---

**Tip:** Always confirm deletions to prevent accidental data loss.