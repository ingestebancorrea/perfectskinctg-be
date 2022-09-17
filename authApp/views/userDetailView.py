from django.conf import settings

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.user import User
from authApp.serializers.userSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)
    
    def put(self,request, pk=None, format=None):
        item = User.objects.get(pk=pk) #obtener item a actualizar
        serializer = UserSerializer(instance=item, data=request.data, partial=True) #Pasar instancia a actualizar y el dato al serializador
        response = Response()
        
        if serializer.is_valid():
            serializer.save()
            response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
            }
            return response
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    #def delete(request,pk):