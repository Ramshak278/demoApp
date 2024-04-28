from django.urls import path
from borrow.borrowapi.views import BorrowingListView, BorrowingbookView, BorrowingRetrieveView, BorrowingUpdateView

urlpatterns = [
    path('borrowlist/', BorrowingListView.as_view()),
    path('borrowbook/create/', BorrowingbookView.as_view()),
    path('borrowretrieve/<int:pk>/', BorrowingRetrieveView.as_view()),
    path('borrowupdate/<int:pk>/update/', BorrowingUpdateView.as_view()),
]
