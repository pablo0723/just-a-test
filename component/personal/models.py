from django.contrib.auth.models import AbstractUser
from django.db import models


class ProfileType(models.Model):
    profile_type = models.CharField(max_length=20)
    description = models.CharField(max_length=50, blank=True, default='')
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['profile_type']

    def __str__(self):
        return self.profile_type.capitalize()


class Title(models.Model):
    title = models.CharField(max_length=20)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title.capitalize()


class Gender(models.Model):
    gender = models.CharField(max_length=20)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['gender']

    def __str__(self):
        return self.gender.capitalize()


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=100)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ethnicity']

    def __str__(self):
        return self.ethnicity.capitalize()


class Profile(AbstractUser):
    title = models.ForeignKey(Title, null=True, on_delete=models.SET_NULL)
    initials = models.CharField(max_length=20, null=True, blank=True, default=None)
    # last_name
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(blank=True, unique=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.SET_NULL)
    ethnicity = models.ForeignKey(Ethnicity, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    # profile type
    profile_type = models.ManyToManyField(ProfileType, default=None)
    terms_and_conditions = models.DateTimeField(null=True, default=None, blank=True)
    # Administrative Fields
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
