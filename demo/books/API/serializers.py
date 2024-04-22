from rest_framework import serializers

from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_date', 'price', 'genre', 'isbn', 'user','image']



class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price', 'genre', 'isbn', 'user','image']

    def create(self, validated_data):
        user = self.context['request'].user
        return Book.objects.create(user=user,**validated_data)


class UpdateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price', 'genre', 'isbn', 'user','image']

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



