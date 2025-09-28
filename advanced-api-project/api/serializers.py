from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    - Serializes all fields.
    - Includes validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    - Serializes the 'name' field.
    - Includes nested BookSerializer to show all related books dynamically.
    """
    books = BookSerializer(many=True, read_only=True)  
    # 'books' comes from related_name in the Book model

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
