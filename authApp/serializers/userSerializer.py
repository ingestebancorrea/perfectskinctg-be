from authApp.models import User, Cliente
from rest_framework import serializers
from .clienteSerializer import ClienteSerializer

class UserSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nombre', 'apellidos', 'tipoDocumento', 'nroDocumento', 'email', 'tipoUsuario','cliente']  # fields [es un arreglo de cadenas]

    #recibe un JSON y lo convierte a objeto, **validated_data: manda argumentos en forma de diccionario
    def create(self, validated_data):
        clienteData = validated_data.pop('cliente') #extrae primera parte del JSON "user" con pop
        userInstance = User.objects.create(**validated_data) #enviar campos restantes
        Cliente.objects.create(user=userInstance,**clienteData) 
        return userInstance
    
    #con los modelos y metodo get se convierte en un unico objeto
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        cliente = Cliente.objects.get(user=obj.id) 
        return{ #return{"contiene objeto de tipo JSON"}
             'id': user.id,
             'username': user.username,
             'password': user.password,
             'nombre': user.nombre,
             'apellidos': user.apellidos,
             'tipoDocumento': user.tipoDocumento,
             'nroDocumento': user.nroDocumento,
             'email': user.email,
             'tipoUsuario': user.tipoUsuario,
             'Cliente':{
                'id': cliente.id
             }
     }

# La relación se controla en el userSerializer, 
# campo cliente con ayuda de UserSerializer, permite manejar la relación entra ambas entidades.

# Sobreescritura de métodos 
# create (crea al cliente con su respectivo usuario simultaneo)