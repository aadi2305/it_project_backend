from rest_framework import serializers
from .models import Users, Address, books , Cart1, Wishlist1, Ordered1





class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name','email')

# class AddToCartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users, books
#         fields = ('name','title')

class CreateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('building','FlatNo','Floor','StreetName','Area','AreaCode','City','State','Landmark')

class searchByNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = ['title']

class searchByGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = ['genre']

class searchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = ("id", 'title', 'author', 'price', 'genre', 'pages', 'paperType', 'rating', 'url')
        # fields = '__all__'

class sendCartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart1
        fields = ("bookFK", "userFK")

class sendWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Wishlist1
        fields = ("bookFK", "userFK")

class orderedListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordered1
        fields = ("userFK", "cartFK")