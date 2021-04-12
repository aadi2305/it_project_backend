from django.db import models
from mongoengine import *
# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    price = models.BigIntegerField()
    genre = models.CharField(max_length=1000)
    pages = models.BigIntegerField()
    paperType = models.CharField(max_length=1000)
    rating = models.FloatField()
    url = models.CharField(max_length=1000)

class Users(models.Model):
    name = models.CharField(max_length=1000)
    surname = models.CharField(max_length=1000)
