from django.urls import path
from .API.views import BookListView, BookCreateView, BookRetrieveView, BookUpdateView, BookByAuthorView, \
    BookByTitleView, BookByUserIdView, BookByBookIdView

urlpatterns = [
    path('list/', BookListView.as_view()),
    path('create/', BookCreateView.as_view()),
    path('<int:pk>/', BookRetrieveView.as_view()),
    path('<int:pk>/update/', BookUpdateView.as_view()),
    path('<str:author_name>/', BookByAuthorView.as_view()),
    path('bybook/<str:book_name>/', BookByTitleView.as_view()),
    path('byuser/<str:user_id>/', BookByUserIdView.as_view()),
    path('byid/<int:book_id>/', BookByBookIdView.as_view()),
]
