from django.shortcuts import render
from django.http import HttpResponse
from .models import books, Users, Address, Cart1, Wishlist1, Ordered1
from rest_framework import generics, status
from .serializers import  CreateUserSerializer, CreateAddressSerializer, searchByNameSerializer, searchResultSerializer, searchByGenreSerializer, sendCartSerializers, sendWishlistSerializer
from rest_framework.views import APIView
import json
from django.db.models import Q
from rest_framework.response import Response
# Create your views here.
def yo(request):
    # f = open('BooksJson.json',)
  
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
    # cart1 = Cart(booksId=12, userId=69)         
    # cart1.save()       
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


def SendAllBooks(request):
    allBooks = books.objects.all()
    convertedList = []
    for book in allBooks:
        convertedList.append(searchResultSerializer(book).data)
    json_object = json.dumps(convertedList, indent = 4) 
    return HttpResponse(json_object)
    


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

class sendCartInfo(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            userId = Users.objects.filter(email = email)
            searchResult = Cart1.objects.filter(userFK = userId[0])
            convertedList = []
            print(convertedList)
            for cart in searchResult:
                searchResultForBooks = books.objects.filter(id = sendCartSerializers(cart).data["bookFK"])
                convertedList.append(searchResultSerializer(searchResultForBooks[0]).data)
            return Response(convertedList, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

# user1 = User(name = "mihir", email = "abc@123.com")
# user1.save()
class addToCartInfo(APIView):
    def post(self, request, format=None):
        data=request.data
        email = data["email"]
        title = data["title"]
        user = Users.objects.filter(email = email)
        book1 = books.objects.filter(title = title)
        newCart = Cart1(bookFK = book1[0], userFK = user[0])
        newCart.save()
        return Response("", status=status.HTTP_200_OK)

#de

class addToWishlist(APIView):
    def post(self, request, format=None):
        data=request.data
        email = data["email"]
        title = data["title"]
        user = Users.objects.filter(email = email)
        book1 = books.objects.filter(title = title)
        newWishlist = Wishlist1(bookFK = book1[0], userFK = user[0])
        newWishlist.save()
        return Response("", status=status.HTTP_200_OK)

class sendWishlistInfo(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            userId = Users.objects.filter(email = email)
            # userId = [mihir]
            searchResult = Wishlist1.objects.filter(userFK = userId[0])
            convertedList = []
            for wishlist in searchResult:
                searchResultForBooks = books.objects.filter(id = sendWishlistSerializer(wishlist).data["bookFK"])
                convertedList.append(searchResultSerializer(searchResultForBooks[0]).data)
            return Response(convertedList, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)



def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

class addToOrderedList(APIView):
    def post(self, request, format=None):
        data=request.data
        email = data["email"]
        title = data["title"]
        user = Users.objects.filter(email = email)
        book1 = books.objects.filter(title = title)
        newOrder = Ordered1(bookFK = book1[0], userFK = user[0])
        newOrder.save()
        deleteCart1 = Cart1.objects.filter(bookFK = book1[0], userFK = user[0])
        deleteCart1.delete()
        return Response("", status=status.HTTP_200_OK)

class removeFromCart(APIView):
    def post(self, request, format=None):
        data=request.data
        email = data["email"]
        title = data["title"]
        user = Users.objects.filter(email = email)
        book1 = books.objects.filter(title = title)
        deleteCart1 = Cart1.objects.filter(bookFK = book1[0], userFK = user[0])
        deleteCart1.delete()
        return Response("", status=status.HTTP_200_OK)


class SendToOrderedList(APIView):
    def post(self, request, format=None):
        data=request.data
        email = data["email"]
        user = Users.objects.filter(email = email)
        bookssss = Ordered1.objects.filter(userFK = user[0])
        convertedList = []
        for wishlist in bookssss:
            searchResultForBooks = books.objects.filter(id = sendWishlistSerializer(wishlist).data["bookFK"])
            convertedList.append(searchResultSerializer(searchResultForBooks[0]).data)
        return Response(convertedList, status=status.HTTP_200_OK)

