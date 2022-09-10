from rest_framework import serializers
from authApp.models import Cliente,User
from authApp.serializers.userSerializer import UserSerializer

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cliente
        fields = ['id', 'user', 'nombre', 'apellidos', 'tipoDocumento', 'nroDocumento', 'sexo', 'telefono', 'email', 'direccion']
    
    def create(self, validated_data):
        userData = validated_data.pop('user')
        clienteInstance = Cliente.objects.create(**validated_data)
        User.objects.create(cliente=clienteInstance, **userData)
        return clienteInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        cliente = Cliente.objects.get(user=obj.id)
        return {
            'id': cliente.id,
            'user': {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'tipoUsuario': user.tipoUsuario
            },
            'nombre': cliente.nombre,
            'apellidos': cliente.apellidos,
            'tipoDocumento': cliente.tipoDocumento,
            'nroDocumento': cliente.nroDocumento,
            'sexo': cliente.sexo,
            'telefono': cliente.telefono,
            'email': cliente.email,
            'direccion': cliente.direccion,
            'estado': cliente.estado,
        }