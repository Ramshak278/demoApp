from django.urls import path

from books.API.views import BookByAuthorView, BookByTitleView, BookByUserIdView
from .Api.views import Registrations, MyTokenObtainPairView, UserRetrieveUpdateAPIView

urlpatterns=[
    path("register",Registrations.as_view()),
    path("login",MyTokenObtainPairView.as_view()),
    path("verify",UserRetrieveUpdateAPIView.as_view())
    path('books/by_author/<str:author_name>/', BookByAuthorView.as_view()),
    path('books/by_title/<str:book_name>/', BookByTitleView.as_view()),
    path('books/by_user/<int:user_id>/', BookByUserIdView.as_view()),
]