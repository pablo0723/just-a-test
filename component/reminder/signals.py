from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from component.reminder.tasks import send_email

from component.reminder.models import Reminder


@receiver(post_save, sender=Reminder)
def send_reminder(sender, instance, **kwargs):
    time_to_send = timezone.now() + timezone.timedelta(minutes=instance.delay)
    send_email.apply_async(args=[instance.id], eta=time_to_send)
