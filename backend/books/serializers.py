from rest_framework import serializers
from .models import Users, Address, books 





class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name','email')

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

