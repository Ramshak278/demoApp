

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_task():
    send_mail(
        'Subject - Scheduled Email',
        'This is the body of the scheduled email.',
        settings.DEFAULT_FROM_EMAIL,
        ['ramshak278@gmail.com'],  # Replace with your recipient email address
        fail_silently=False,
    )
