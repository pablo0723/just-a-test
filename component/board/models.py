from django.db import models
from django_extensions.db.fields import AutoSlugField


class Board(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['slug']


class TodoTask(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='todos')
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['board']
