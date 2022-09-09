from rest_framework import serializers
from authApp.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['balance', 'lastChangeDate', 'isActive']