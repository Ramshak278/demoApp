from django.urls import path
from .API.views import BookListView, BookCreateView, BookRetrieveView, BookUpdateView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/create/', BookCreateView.as_view()),
    path('books/<int:pk>/', BookRetrieveView.as_view()),
    path('books/<int:pk>/update/', BookUpdateView.as_view()),
]
