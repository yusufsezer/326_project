from django.db import models
from django import forms

class User(models.Model):
    """Model representing a User."""

    username = models.CharField(
        max_length=20, help_text="Enter a book genre (e.g. Science Fiction)"
    )

    password = models.CharField(
        max_length=20, help_text="Enter your password"
    )

    sessions = models.ForeignKey("Session", on_delete=models.SET_NULL, null=True)

    # sessions_owned = models.ForeignKey("Session", on_delete=models.SET_NULL, null=True)

    games = models.ForeignKey("Game", on_delete=models.SET_NULL, null=True)

    platforms = models.ForeignKey("Platform", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.username

class Session(models.Model):
    """Model representing a Session."""

    # TODO: IMPLEMENT THIS CLASS

    def __str__(self):
        """String for representing the Model object."""
        return ""

class Game(models.Model):
    """Model representing a Game."""

    # TODO: IMPLEMENT THIS CLASS

    def __str__(self):
        """String for representing the Model object."""
        return ""

class Platform(models.Model):
    """Model representing a Platform."""

    # TODO: IMPLEMENT THIS CLASS

    def __str__(self):
        """String for representing the Model object."""
        return ""
