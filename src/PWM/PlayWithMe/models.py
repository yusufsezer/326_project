import uuid

from datetime import datetime
from django.db import models
from django import forms

from django.urls import reverse
from django.contrib.auth.models import User  # NEW 10
from datetime import date  # NEW 10

class Profile(models.Model):
    """Model representing a Profile."""

    username = models.CharField(
        max_length=20,
        help_text="The Profile's username"
    )

    password = models.CharField(
        max_length=20,
        help_text="The profile's password"
    )

    # sessions = models.ManyToManyField(
    #     "Session",
    #      on_delete=models.SET_NULL,
    #      null=True,
    #      related_name="sessions",
    #      blank=True
    # )

    sessions = models.ManyToManyField(
        "Session",
        related_name="sessions",
        blank=True
    )

    # sessions_owned = models.ForeignKey(
    #     "Session",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name="sessions_owned",
    #     blank=True
    # )

    sessions_owned = models.ManyToManyField(
        "Session",
        related_name="sessions_owned",
        blank=True
    )

    # games = models.ForeignKey(
    #     "Game",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    games = models.ManyToManyField(
        "Game",
        blank=True
    )

    # platforms = models.ForeignKey(
    #     "Platform",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    platforms = models.ManyToManyField(
        "Platform",
        blank=True
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.username

class Session(models.Model):
    """Model representing a Session."""

    id = models.CharField(
        max_length=60,
        help_text="ID to uniquely identify a session",
        primary_key=True
    )

    profiles = models.ManyToManyField(
        "Profile"
    )

    owner = models.OneToOneField(
        "Profile",
        on_delete=models.SET_NULL,
        null=True,
        related_name="owner"
    )

    # games = models.ForeignKey(
    #     "Game",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    games = models.ManyToManyField(
        "Game",
        blank=True
    )

    # platforms = models.ForeignKey(
    #     "Platform",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    platforms = models.ManyToManyField(
        "Platform",
        blank=True
    )

    messages = models.ForeignKey(
        "Message",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=100,
        help_text="The session's location",
        default=""
    )

    online = models.BooleanField(default=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.id

class Game(models.Model):
    """Model representing a Game."""

    title = models.CharField(
        max_length=100,
        help_text="The game's title",
        default=""
    )

    # platforms = models.ForeignKey(
    #     "Platform",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    platforms = models.ManyToManyField(
        "Platform",
        blank=True
    )

    online = models.BooleanField(default=True)

    description = models.CharField(
        max_length=100,
        help_text="The game's description",
        default=""
    )

    link = models.CharField(
        max_length=100,
        help_text="A link to this game's website",
        default=""
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Platform(models.Model):
    """Model representing a Platform."""
    #
    # id = models.CharField(
    #     max_length=60,
    #     help_text="ID to uniquely identify a platform",
    #     primary_key=True
    # )

    name = models.CharField(
        max_length=100,
        help_text="The name of the platform (e.g. PlayStation 4)",
        default=""
    )

    # games = models.ForeignKey(
    #     "Game",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True
    # )

    games = models.ManyToManyField(
        "Game",
        blank=True
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Message(models.Model):
    """Model representing a Message."""

    text = models.CharField(
        max_length=100,
        help_text="The text content of the message",
        default=""
    )

    sender = models.ForeignKey(
        "Profile",
        on_delete=models.SET_NULL,
        null=True
    )

    context = models.ForeignKey(
        "Session",
        on_delete=models.SET_NULL,
        null=True
    )

    # context = models.ForeignKey(
    #     "Session",
    #     on_delete=models.SET_NULL,
    #     null=True
    # )

    datetime = models.DateTimeField(
        default=datetime.now,
        blank=True
    )

    def __str__(self):
        """String for representing the Model object."""
        return f"Message from: {self.sender} with text: {self.text}"
