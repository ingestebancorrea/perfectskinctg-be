from rest_framework import serializers
from authApp.models import Cliente,User
from authApp.serializers.userSerializer import UserSerializer

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cliente
        fields = ['cliente_codigo', 'user', 'nombre', 'apellidos', 'tipoDocumento', 'nroDocumento', 'Telefono', 'Email', 'Direccion']
    
    def create(self, validated_data):
        clienteData = validated_data.pop('cliente')
        userInstance = User.objects.create(**validated_data)
        Cliente.objects.create(user=userInstance, **clienteData)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        cliente = Cliente.objects.get(user=obj.id)
        return {
            'cliente_codigo': cliente.cliente_codigo,
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
            'telefono': cliente.telefono,
            'email': cliente.email,
            'direccion': cliente.direccion,
            'estado': cliente.estado,
        }