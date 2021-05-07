from django.core.mail import send_mail

from component.reminder.models import Reminder
from server.celery import app


@app.task
def send_email(id):
    reminder = Reminder.objects.filter(id=id).first()
    if reminder is not None:
        send_mail(subject="ReminderMessage",
                  message=reminder.text,
                  from_email='no-reply@test.com',
                  recipient_list=[reminder.email]
                  )
