# Creating a Django App: Bookshelf

This guide walks you through creating a new Django app called `bookshelf` within your Django project.

## 1. Create the App

Run the following command in your project directory:

```bash
python manage.py startapp bookshelf
```

## 2. Register the App

Add `'bookshelf'` to the `INSTALLED_APPS` list in your `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'bookshelf',
]
```

## 3. Define Models

Edit `bookshelf/models.py` to define your models. Example:

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
```

## 4. Apply Migrations

```bash
python manage.py makemigrations bookshelf
python manage.py migrate
```

## 5. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

## 6. Register Models in Admin

Edit `bookshelf/admin.py`:

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)
```

---

Your `bookshelf` app is now set up!