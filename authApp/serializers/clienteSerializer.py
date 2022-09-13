from rest_framework import serializers
from authApp.models import Cliente,User
from .userSerializer import UserSerializer

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellidos', 'tipoDocumento', 'nroDocumento', 'sexo', 'telefono', 'email', 'direccion','estado', 'user']
    
    #recibe un JSON y lo convierte a objeto, **validated_data: manda argumentos en forma de diccionario
    def create(self, validated_data):
        userData = validated_data.pop('user') #extrae primera parte del JSON "user" con pop
        clienteInstance = Cliente.objects.create(**validated_data) #enviar campos restantes
        User.objects.create(cliente=clienteInstance,**userData) 
        return clienteInstance
    
    #con los modelos y metodo get se convierte en un unico objeto
    def to_representation(self, obj):
        cliente = Cliente.objects.get(id=obj.id)
        user = User.objects.get(cliente=obj.id)
        #return{"contiene objeto de tipo JSON"}
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
            }
        }
        
# La relación se controla en el clienteSerializer, 
# campo user con ayuda de UserSerializer, permite manejar la relación entra ambas entidades.

# Sobreescritura de métodos 
# create (crea al cliente con su respectivo usuario simultaneo)