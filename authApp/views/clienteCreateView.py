from rest_framework import views, status
from rest_framework.response import Response
from authApp.serializers.clienteSerializer import ClienteSerializer

class ClienteCreateView(views.APIView):
    def post(self, request):
        cliente_serializer = ClienteSerializer(data = request.data) #deserializa convierte en objeto
        
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cliente_serializer.errors, status = status.HTTTP_400_BAD_REQUEST)
    
#variable data guarda la información serializada la guarda en JSON