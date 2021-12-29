# soundboard/models.py
# Models used for soundboard website
# Last Modified: 12/28/2021

from django.db import models
from django.contrib import admin

# character field length constants
MAX_LENGTH_NAME = 500
MAX_LENGTH_DESCRIPTION = 10000


# Models dealing with soundboards
class SoundboardCategory(models.Model):
    """
    Represents a soundboard category (ex. Taconic Shows)
    Fields: category_name
    When converted to a string, category name is used
    """
    category_name = models.CharField(max_length=MAX_LENGTH_NAME)

    # returns category name when converted to a string
    def __str__(self):
        return self.category_name

    # custom name information
    class Meta:
        verbose_name = "Soundboard Category"
        verbose_name_plural = "Soundboard Categories"


class Soundboard(models.Model):
    """
    Represents a soundboard with sounds
    Fields: category, soundboard_name, soundboard_image, soundboard_description
    When converted to a string, soundboard name is used
    """
    # category that the soundboard belongs to
    category = models.ForeignKey(SoundboardCategory, on_delete=models.CASCADE)
    # name of soundboard
    soundboard_name = models.CharField(max_length=MAX_LENGTH_NAME)
    # soundboard image to be shown
    soundboard_image = models.ImageField(upload_to=f'images/')
    # soundboard description
    soundboard_description = models.CharField(max_length=MAX_LENGTH_DESCRIPTION)

    # returns soundboard name when converted to a string
    def __str__(self):
        return self.soundboard_name


# Models dealing with sounds
class SoundCategory(models.Model):
    """
    Represents a category of sounds
    Fields: soundboard, category_name
    When converted to a string, category_name is used
    """
    # soundboard that category belongs to
    soundboard = models.ForeignKey(Soundboard, on_delete=models.CASCADE)
    # name of category
    category_name = models.CharField(max_length=MAX_LENGTH_NAME)

    def __str__(self):
        return self.category_name

    # custom name information
    class Meta:
        verbose_name = "Sound Category"
        verbose_name_plural = "Sound Categories"


class Sound(models.Model):
    """
    Represents a sound that can be played on the soundboard
    Fields: category, sound_name, sound_file
    When converted to a string, sound name is used
    """
    # sound category that sound belongs to
    category = models.ForeignKey(SoundCategory, on_delete=models.CASCADE)
    # name of sound
    sound_name = models.CharField(max_length=MAX_LENGTH_NAME)
    # sound file location
    sound_file = models.FileField(upload_to=f'sounds/')

    def __str__(self):
        return self.sound_name

