from rest_framework import serializers
from authApp.models import Cita
#<<<<<<< Updated upstream


from django import forms
#>>>>>>> Stashed changes

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id', 'fecha', 'hora', 'lugar', 'cliente', 'empleado', 'servicio', 'estado']