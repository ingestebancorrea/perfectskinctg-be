from rest_framework import views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.clienteSerializer import ClienteSerializer

class ClienteCreateView(views.APIView):
    def post(self, request):
        cliente_serializer = ClienteSerializer(data = request.data) #deserializa convierte en objeto
        
        if cliente_serializer.is_valid():
            cliente_serializer.save()
            return Response(cliente_serializer.data)
        return Response(cliente_serializer.errors)
    
#variable data guarda la información serializada porque la guarda en JSON