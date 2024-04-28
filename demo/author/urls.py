from django.urls import path
from author.authapi.views import AuthorListView, AuthorCreateView, AuthorRetrieveView, AuthorUpdateView

urlpatterns = [
    path('authlist/', AuthorListView.as_view()),
    path('authcreate/', AuthorCreateView.as_view()),
    path('authretrieve/<int:pk>/', AuthorRetrieveView.as_view()),
    path('authupdate/<int:pk>/update/', AuthorUpdateView.as_view()),
]
