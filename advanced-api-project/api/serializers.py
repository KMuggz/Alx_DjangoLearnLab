from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    # serializes all fields of Book model
    # includes custom validation for publication year
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # serializes the Author name and dynamically includes a nested list of their related books
    # the 'books' field matches the related_name in the Book model
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']


"""
Nested Serialization: By adding books = BookSerializer(many=True, read_only=True) to the AuthorSerializer, the API will return an array of book objects whenever an author is retrieved.

Custom Validation: The validate_publication_year method is a field-level validator that automatically checks the data before it is saved to the database.
"""