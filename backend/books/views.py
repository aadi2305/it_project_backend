from django.shortcuts import render
from django.http import HttpResponse
from .models import books, Users
from rest_framework import generics, status
from .serializers import  CreateRoomSerializer
from rest_framework.views import APIView
import json
from rest_framework.response import Response
# Create your views here.
def yo(request):
    all_entries = books.objects.all()
    return HttpResponse(all_entries)


          
class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            surname = serializer.data.get('surname')
            user1 = Users(name = name, surname = surname)
            user1.save()
            return Response(CreateRoomSerializer(user1).data, status=status.HTTP_200_OK)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)    