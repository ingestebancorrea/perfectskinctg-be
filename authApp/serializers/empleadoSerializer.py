from rest_framework import serializers
from authApp.models import Empleado,User
from authApp.serializers.userSerializer import UserSerializer

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['balance', 'lastChangeDate', 'isActive']
    
    def create(self, validated_data):
        empleadoData = validated_data.pop('empleado')
        userInstance = User.objects.create(**validated_data)
        Empleado.objects.create(user=userInstance, **empleadoData)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        empleado = Empleado.objects.get(user=obj.id)
        return {
            'empleado_codigo': empleado.empleado_codigo,
            'user': {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'tipoUsuario': user.tipoUsuario
            },
            'cargo': empleado.cargo,
            'nombre': empleado.nombre,
            'apellidos': empleado.apellidos,
            'tipoDocumento': empleado.tipoDocumento,
            'nroDocumento': empleado.nroDocumento,
            'sexo': empleado.sexo,
            'telefono': empleado.telefono,
            'email': empleado.email,
            'direccion': empleado.direccion,
            'estado': empleado.estado,
        }