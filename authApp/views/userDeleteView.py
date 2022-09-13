from rest_framework.response import Response
from rest_framework import views
from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserDeleteView(views.APIView):
    def delete(request, pk=None):
        user = User.objects.filter(id = pk).first() #llamar consulta
        user.delete() 
        return Response('Eliminado') 

# APIView es una clase implementada por Django REST que contiene la configuración inicial necesaria para
# que Django perciba a cualquier clase como una vista.