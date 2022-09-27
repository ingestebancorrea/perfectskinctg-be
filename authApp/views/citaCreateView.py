from rest_framework import status, views
from authApp import serializers
from authApp.models import Cita
from authApp.serializers import CitaSerializer
from rest_framework.response import Response

class CitaCreateView(views.APIView):
    def post(self,request,format=None):
        item = request.data
        serializer = CitaSerializer(data=item)
        
        serializer.is_valid(raise_exception=True) #Verificando si es valido
        serializer.save() #Crear en DB
        
        response = Response()

        response.data = {
            'message': 'Created Successfully',
            'data': serializer.data
        }

        return response