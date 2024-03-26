from django.urls import path

from .Api.views import Registrations, MyTokenObtainPairView, UserRetrieveUpdateAPIView

urlpatterns=[
    path("register",Registrations.as_view()),
    path("login",MyTokenObtainPairView.as_view()),
    path("verify",UserRetrieveUpdateAPIView.as_view())
]