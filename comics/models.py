from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class superheroPowerstats(models.Model):
    name = models.CharField(max_length = 100)
    intelligence = models.IntegerField()
    strength = models.IntegerField()
    speed = models.IntegerField()
    durability = models.IntegerField()
    power = models.IntegerField()
    combat = models.IntegerField()

class superheroAppearance(models.Model):
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 40)
    race = models.CharField(max_length = 60)
    height = models.CharField(max_length = 60)
    weight = models.CharField(max_length = 60)
    eyeColor = models.CharField(max_length = 40)
    hairColor = models.CharField(max_length = 40)

class superheroBiography(models.Model):
    name = models.CharField(max_length = 100)
    fullName = models.CharField(max_length = 100)
    alterEgos = models.CharField(max_length = 250)
    aliases = models.CharField(max_length = 250)
    birthPlace = models.CharField(max_length = 100)
    firstAppearance = models.CharField(max_length = 250)
    publisher = models.CharField(max_length = 100)
    alignment = models.CharField(max_length = 50, default = "neutral")

class superheroWork(models.Model):
    name = models.CharField(max_length = 100)
    occupation = models.CharField(max_length = 500)
    base = models.CharField(max_length = 250)

class superheroConnections(models.Model):
    name = models.CharField(max_length = 100)
    groupAffiliation = models.CharField(max_length = 1000)
    relatives = models.CharField(max_length = 1000)

class superheroImages(models.Model):
    name = models.CharField(max_length = 100)
    small = models.ImageField(upload_to = 'images')
    medium = models.ImageField(upload_to = 'images')
    large = models.ImageField()
