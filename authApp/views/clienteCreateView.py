from rest_framework.views import APIView, status
from rest_framework.response import Response

from authApp.serializers.clienteSerializer import ClienteSerializer

class ClienteCreateView(APIView):
    def post(self, request):
        cliente = ClienteSerializer(data=request.data)
        
        if cliente.is_valid():
            cliente.save()
            return Response(cliente.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
#variable data guarda la información serializada la guarda en JSON