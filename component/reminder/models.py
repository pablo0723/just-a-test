from django.db import models

from component.personal.models import Profile


class Reminder(models.Model):
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE) Not specified in task just in case
    email = models.EmailField(max_length=250)
    text = models.TextField()
    delay = models.IntegerField(default=0)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['email']
