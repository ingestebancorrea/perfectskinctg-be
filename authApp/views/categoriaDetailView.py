from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from authApp.models.categoria import Categoria
from authApp.serializers.categoriaSerializer import CategoriaSerializer

class CategoriaDetailView(APIView):
    def get(self, request,pk):
        item = self.get_object().categoria.all()
        serializer =  CategoriaSerializer(item, many=True)
        return Response(serializer.data)
    
#     def put(self,request, pk):
#         item = User.objects.get(pk=pk) #obtener item a actualizar
#         serializer = UserSerializer(instance=item, data=request.data, partial=True) #Pasar instancia a actualizar y el dato al serializador, partial nos permitirá actualizar sin pasar todo el objeto
#         response = Response()
        
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         response = Response()

#         response.data = {
#             'message': 'Todo Updated Successfully',
#             'data': serializer.data
#         }

#         return response

#     def delete(self,request,pk):
#         item = User.objects.get(pk=pk)
#         item.delete()
        
#         return Response({
#             'message': 'User Deleted Successfully'
#         })