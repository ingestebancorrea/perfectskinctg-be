from rest_framework import serializers
from authApp.models import Cliente,User
from .userSerializer import UserSerializer

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Cliente
        fields = ['id','user']
    
    #recibe un JSON y lo convierte a objeto, **validated_data: manda argumentos en forma de diccionario
    def create(self, validated_data):
        userData = validated_data.pop('user') #extrae primera parte del JSON "user" con pop
        clienteInstance = Cliente.objects.create(**validated_data) #enviar campos restantes
        User.objects.create(cliente=clienteInstance,**userData) 
        return clienteInstance
    
    #con los modelos y metodo get se convierte en un unico objeto
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        cliente = Cliente.objects.get(user=obj.id) 
        return { #return{"contiene objeto de tipo JSON"}
            'id': cliente.id,
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
        
# La relación se controla en el clienteSerializer, 
# campo user con ayuda de UserSerializer, permite manejar la relación entra ambas entidades.

# Sobreescritura de métodos 
# create (crea al cliente con su respectivo usuario simultaneo)