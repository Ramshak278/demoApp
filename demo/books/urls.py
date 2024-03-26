
from django.contrib import admin
from django.urls import path,include,re_path
from .views import addBook,editBook,editBookView,deleteBookView

urlpatterns = [
    path("add-book/add",addBook),
    path("edit-book/",editBookView),
    path("edit-book/edit",editBook),
    path("delete-book",deleteBookView)
]