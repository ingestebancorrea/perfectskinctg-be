from authApp.models import Servicio
from rest_framework import serializers

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['nombre', 'precio', 'estado']