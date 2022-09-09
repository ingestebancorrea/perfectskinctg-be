from authApp.models.cita import Cita
from rest_framework import serializers

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['cita_codigo', 'fecha', 'hora', 'lugar_servicio', 'cliente', 'empleado', 'estado']