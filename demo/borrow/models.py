# Create your models here.
from django.db import models
from demoapp.models import User
from books.models import Book
from django.utils import timezone


class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateField(default=timezone.now)
    due_date = models.DateField()
    return_status = models.CharField(max_length=10, choices=[('borrowed', 'Borrowed'), ('returned', 'Returned')])

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
