from django.db import models
from books.models import Book


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    website = models.URLField(null=True, blank=True)
    social_media = models.CharField(max_length=100, null=True, blank=True)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return self.name
