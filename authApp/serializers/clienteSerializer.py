from rest_framework import serializers
from authApp.models import Cliente,User

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        #fields = ['id','user']