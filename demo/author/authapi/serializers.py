from rest_framework import serializers
from author.models import Author
from books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price', 'genre', 'isbn', 'user', 'isDeleted', 'creation_time', 'deletion_time', 'image']

class AuthorSerializer(serializers.ModelSerializer):
    # Include the nested BookSerializer to represent the Many-to-Many relationship
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'website', 'social_media', 'books']
