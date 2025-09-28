from django.db import models

# Author model stores information about book authors.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Book model stores information about books and links to Author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title} ({self.publication_year})"

# Relationship: One Author can have many Books (one-to-many via ForeignKey).
# The 'related_name' allows reverse access from Author to their books.
