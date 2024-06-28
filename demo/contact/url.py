from django.urls import path
from .api.views import contact_us

urlpatterns = [
    path('contact-us/', contact_us, name='contact_us'),
]
