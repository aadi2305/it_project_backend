from django.db import models
from mongoengine import *
import uuid

# Create your models here.
class books(models.Model):
    #bookId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    price = models.BigIntegerField()
    genre = models.CharField(max_length=1000)
    pages = models.BigIntegerField()
    paperType = models.CharField(max_length=1000)
    rating = models.FloatField()
    url = models.CharField(max_length=1000)

class Users(models.Model):
    #userId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    name = models.CharField(max_length=1000, null=False)
    #surname = models.CharField(max_length=1000)
    email = models.EmailField(max_length=254, null=False, default='abc@123.com')

class Address(models.Model):
    #addressId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=False)
    #addressFK = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    building = models.CharField(max_length=100, null=False)
    FlatNo = models.IntegerField()
    Floor = models.IntegerField()
    StreetName = models.CharField(max_length=100)
    Area = models.CharField(max_length=100, null=False)
    AreaCode = models.BigIntegerField()
    City = models.CharField(max_length=100, null=False)
    State = models.CharField(max_length=100, null=False)
    Landmark = models.CharField(max_length=100)

class Cart1(models.Model):
    bookFK = models.ForeignKey(books, on_delete=models.CASCADE, blank=True, null=True)
    userFK = models.ForeignKey(Users,on_delete=models.CASCADE, blank=True, null=True)
    #We need a Model which will add the particular books that the user adds to his/her cart.

class Wishlist1(models.Model):
    bookFK = models.ForeignKey(books, on_delete=models.CASCADE, blank=True, null=True)
    userFK = models.ForeignKey(Users,on_delete=models.CASCADE, blank=True, null=True)
    # bookwishFK = models.ForeignKey(books,on_delete=models.CASCADE, blank=True, null=True)
    #The wishlist will be referencing the cartId and also the userId.

class Ordered1(models.Model):
    Status = models.BooleanField(default=False)
    userFK = models.ForeignKey(Users,on_delete=models.CASCADE, blank=True, null=True)
    bookFK = models.ForeignKey(books, on_delete=models.CASCADE, blank = True, null= True)
    # orderedBooksFK = models.ForeignKey(books,on_delete=models.CASCADE, blank=True, null=True)
    # userFK = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    #The wishlist will be referencing the cartId and also the userId.

