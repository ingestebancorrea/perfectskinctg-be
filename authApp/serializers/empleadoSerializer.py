from rest_framework import serializers
from authApp.models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'cargo', 'user']