from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils.timesince import timesince


class MyUser(AbstractUser):
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    # avatar = models.ImageField(null=True, default='')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


# Type (Movie or Series)
class Type(models.Model):
    MOVIE = 'Movie'
    SERIES = 'Series'

    CHOICES = [
        (MOVIE, 'Movie'),
        (SERIES, 'Series'),
    ]
    name = models.CharField(max_length=200, choices=CHOICES, help_text='Choose between Movie or Series')

    def __str__(self):
        return self.get_name_display()


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Room Model
class Room(models.Model):
    host = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    room_type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(MyUser, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return str(self.name)

    def get_creation_activity(self):
        return f'Created a room "{self.name}"'


# Comments Model
class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

    def get_activity(self):
        return f'Commented on room "{self.room.name}" with "{self.body}"'
