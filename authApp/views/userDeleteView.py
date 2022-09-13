from rest_framework.response import Response
from rest_framework import generics
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserDeleteView(generics.RetrieveAPIView):
    def delete(request, pk=None):
        user = User.objects.filter(id = pk).first() #llamar consulta
        user.delete() 
        return Response('Eliminado') 