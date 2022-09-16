from rest_framework import serializers
from authApp.models import Cliente,User
from .userSerializer import UserSerializer

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cliente
        fields = ['id','user']