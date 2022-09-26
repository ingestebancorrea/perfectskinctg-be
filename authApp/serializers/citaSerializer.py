from rest_framework import serializers
from authApp.models import Cita

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id', 'fecha', 'hora', 'lugar', 'cliente', 'empleado', 'servicio', 'estado']