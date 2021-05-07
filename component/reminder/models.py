from django.db import models


class Reminder(models.Model):
    email = models.EmailField(max_length=250)
    text = models.TextField()
    delay = models.IntegerField(default=0)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)