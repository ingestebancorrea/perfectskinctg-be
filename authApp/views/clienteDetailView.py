from django.conf import settings

from rest_framework import status
from rest_framework.response import Response

from authApp.models.cliente import Cliente
from authApp.serializers.clienteSerializer import ClienteSerializer

class ClienteDetailView(generics.RetrieveAPIView):
    def get(self, request):
        cliente = Cliente.objects.filter(id = pk).first()
        cliente_serializer = ClienteSerializer(cliente)
        return Response(cliente_serializer.data)     