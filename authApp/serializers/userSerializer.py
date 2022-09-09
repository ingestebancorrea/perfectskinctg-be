from rest_framework import serializers
from authApp.models import Account,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'tipoUsuario']