from django.utils import timezone

from django.db import models

from demoapp.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    isDeleted = models.BooleanField(default=False)
    creation_time = models.DateTimeField(default=timezone.now)
    deletion_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
