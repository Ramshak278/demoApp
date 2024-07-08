from celery import shared_task

@shared_task
def send_reminder_notification():
    # Logic to send notification (could be an email, SMS, push notification, etc.)
    print("Time to stay active! Take a break and move around!")
