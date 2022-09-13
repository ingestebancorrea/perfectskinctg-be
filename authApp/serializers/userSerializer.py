from authApp.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nombre', 'apellidos', 'tipoDocumento', 'nroDocumento', 'email', 'tipoUsuario']         # fields [es un arreglo de cadenas]

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return{
            'user': {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'nombre': user.nombre,
            'apellidos': user.apellidos,
            'tipoDocumento': user.tipoDocumento,
            'nroDocumento': user.nroDocumento,
            'email': user.email,
            'tipoUsuario': user.tipoUsuario
            }
        }