from rest_framework import serializers
from authApp.models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Empleado
        fields = ['id', 'cargo', 'user']