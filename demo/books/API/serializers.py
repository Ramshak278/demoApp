from rest_framework import serializers

from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'price', 'genre', 'isbn', 'user']


class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price', 'genre', 'isbn', 'user']

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class UpdateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price', 'genre', 'isbn', 'user']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.price = validated_data.get('price', instance.price)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance



