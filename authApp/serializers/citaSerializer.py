from rest_framework import serializers
from authApp.models import Cita
from django import forms

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id', 'fecha', 'hora', 'lugar', 'cliente', 'empleado', 'servicio', 'estado']
        
    def clean_validation(self):
        fecha = self.clean_data.get('fecha')
        hora = self.clean_data.get('hora')
        if Cita.objects.filter(fecha=fecha).exists() and Cita.objects.filter(hora=hora).exists():
            raise forms.ValidationError('La fecha y hora seleccionada ya se encuentra agendada')
        return fecha,hora