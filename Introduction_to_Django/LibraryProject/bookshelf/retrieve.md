# Retrieving

In Django, retrieving data from the database is typically done using QuerySets. You can use the ORM (Object-Relational Mapping) to fetch records from your models.

## Basic Retrieval

To retrieve all objects from a model:

```python
from .models import Book

books = Book.objects.all()
```

## Filtering Data

To filter objects based on certain criteria:

```python
available_books = Book.objects.filter(is_available=True)
```

## Retrieving a Single Object

To get a single object, use `get()`:

```python
book = Book.objects.get(id=1)
```

> **Note:** `get()` will raise an error if no object or more than one object is found.

## Ordering Results

You can order results using `order_by()`:

```python
books = Book.objects.order_by('title')
```

## Limiting Results

To limit the number of results:

```python
books = Book.objects.all()[:5]
```

Refer to the [Django QuerySet documentation](https://docs.djangoproject.com/en/stable/topics/db/queries/) for more details.