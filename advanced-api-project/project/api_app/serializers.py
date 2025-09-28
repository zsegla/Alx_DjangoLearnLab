from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    # Custom validation for publication_year
    def validate_publication_year(self, value):
        from datetime import datetime
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

# AuthorSerializer includes nested BookSerializer for related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

"""
BookSerializer: Serializes all fields of Book and validates publication_year.
AuthorSerializer: Serializes Author's name and includes nested books using BookSerializer.
The relationship is handled via the 'books' related_name in the Book model's ForeignKey.
"""
