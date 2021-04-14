from django.shortcuts import render
from django.http import HttpResponse
from .models import books, Users, Address
from rest_framework import generics, status
from .serializers import  CreateUserSerializer, CreateAddressSerializer, searchByNameSerializer, searchResultSerializer, searchByGenreSerializer
from rest_framework.views import APIView
import json
from rest_framework.response import Response
# Create your views here.
def yo(request):
    f = open('BooksJson.json',)
  
    # returns JSON object as 
    # a dictionary
    # data = json.load(f)
    # for Ebook in data:
    #     firstbook = books(title=Ebook["Title"],
    #                       author = Ebook["Author"],
    #                       price=Ebook["Price"],
    #                       genre=Ebook["Genre"],
    #                       pages=Ebook["Pages"],
    #                       paperType=Ebook["Type"],
    #                       rating=Ebook["GoodReadsRating"],
    #                       url=Ebook["URL"])
    #     firstbook.save()                 
    return HttpResponse("Hello")


          
class CreateUser(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            email = serializer.data.get('email')
            user1 = Users(name = name, email = email)
            user1.save()
            return Response(CreateUserSerializer(user1).data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)    

class CreateAddress(APIView):
    serializer_class = CreateAddressSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            building = serializer.data.get('building')
            FlatNo = serializer.data.get('FlatNo')
            Floor = serializer.data.get('Floor')
            StreetName = serializer.data.get('StreetName')
            Area = serializer.data.get('Area')
            AreaCode = serializer.data.get('AreaCode')
            City = serializer.data.get('City')
            State = serializer.data.get('State')
            Landmark = serializer.data.get('Landmark')
            address = Address(building=building, FlatNo=FlatNo, Floor=Floor,StreetName=StreetName, Area=Area, AreaCode=AreaCode, City=City, State=State, Landmark=Landmark)
            address.save()
            return Response(CreateAddressSerializer(address).data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class searchByName(APIView):
    serializer_class = searchByNameSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            title = serializer.data.get('title')
            searchResult = books.objects.filter(title = title)
            return Response(searchResultSerializer(searchResult[0]).data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class searchByGenre(APIView):
    serializer_class = searchByGenreSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            genre = serializer.data.get('genre')
            searchResult = books.objects.filter(genre = genre)
            convertedList = []
            for book in searchResult:
                convertedList.append(searchResultSerializer(book).data)
            return Response(convertedList, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
