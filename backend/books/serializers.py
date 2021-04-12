from rest_framework import serializers
from .models import Users





class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name', 'surname')