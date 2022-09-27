from rest_framework import serializers
from authApp.models import Empleado
from .userSerializer import UserSerializer

class EmpleadoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Empleado
        fields = ['id', 'cargo', 'user']