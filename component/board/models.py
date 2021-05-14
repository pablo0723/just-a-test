from django.db import models
from django_extensions.db.fields import AutoSlugField

from component.personal.models import Profile


class Board(models.Model):
    # owner = models.ForeignKey(Profile, on_delete=models.CASCADE) Not specified in task just in case
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True)
    # member = models.ManyToManyField(Profile) Not specified in task just in case
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['slug']

    @property
    def todos_count(self):
        return self.todos.count()


class TodoTask(models.Model):
    # created_by = models.ForeignKey(Profile, related_name='created_by', on_delete=models.CASCADE) Not specified in task just in case
    # assigned = models.ForeignKey(Profile, related_name='assigned', on_delete=models.CASCADE) Not specified in task just in case
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='todos')
    name = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['board']
