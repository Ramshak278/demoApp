from django.core.mail import send_mail, get_connection, EmailMessage
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from django.template.loader import render_to_string
import datetime

@api_view(['POST'])
def contact_us(request):
    data = request.data
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    if not all([name, email, subject, message]):
        return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

    # Current time
    current_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")

    # Email to admin
    admin_subject = f"New Contact Us Message from {name}"
    admin_message = render_to_string('email.html', {
        'title': 'New Contact Us Message',
        'content': f"User {name} with email {email} has sent a message with the subject '{subject}' and the following message: '{message}' at {current_time}."
    })

    with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS
    ) as connection:
        subject = 'request.POST.get("email")'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST.get("email"), ]
        message = 'request.POST.get("message")'
        EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
    # send_mail('email', 'hello', 'contact@confiatech.com', ["ramshak278@gmail.com"]
    #
    #           )
    # send_mail(
    #
    #
    #     admin_subject,
    #     '',
    #     settings.EMAIL_HOST_USER,
    #     [settings.EMAIL_HOST_USER],
    #     html_message=admin_message
    # )

    # Email to user
    # user_subject = "We have received your message"
    # user_message = render_to_string('email.html', {
    #     'title': 'Message Received',
    #     'content': f"Dear {name}, we have received your message with the subject '{subject}'. Our team will contact you soon."
    # })
    # send_mail(
    #     user_subject,
    #     '',
    #     settings.EMAIL_HOST_USER,
    #     [email],
    #     html_message=user_message
    # )

    return Response({'message': 'Your message has been sent successfully.'}, status=status.HTTP_200_OK)
