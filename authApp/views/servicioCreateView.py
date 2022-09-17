from rest_framework import status, views
from rest_framework.response import Response

from authApp.serializers.servicioSerializer import ServicioSerializer

class ServicioCreateView(views.APIView):
    def post(self,request):
        item = request.data
        serializer = ServicioSerializer(data=item)
        
        serializer.is_valid(raise_exception=True) #Verificando si es valido
        serializer.save() #Crear en DB
        
        response = Response()

        response.data = {
            'message': 'Todo Created Successfully',
            'data': serializer.data
        }

        return response