from rest_framework import serializers
from authApp.models import Cliente,User
from authApp.serializers.userSerializer import UserSerializer

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellidos', 'tipoDocumento', 'nroDocumento', 'sexo', 'telefono', 'email', 'direccion','estado', 'user']
    
    def create(self, validated_data):
        userData = validated_data.pop('user')
        clienteInstance = Cliente.objects.create(**validated_data)
        User.objects.create(cliente=clienteInstance, **userData)
        return clienteInstance
    
    def to_representation(self, obj):
        cliente = Cliente.objects.get(id=obj.id)
        user = User.objects.get(id=obj.id)
        return {
            'id': cliente.id,
            'nombre': cliente.nombre,
            'apellidos': cliente.apellidos,
            'tipoDocumento': cliente.tipoDocumento,
            'nroDocumento': cliente.nroDocumento,
            'sexo': cliente.sexo,
            'telefono': cliente.telefono,
            'email': cliente.email,
            'direccion': cliente.direccion,
            'estado': cliente.estado,
            'user': {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'tipoUsuario': user.tipoUsuario
            }
        }