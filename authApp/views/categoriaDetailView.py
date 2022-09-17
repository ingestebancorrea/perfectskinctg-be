from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from authApp.models.categoria import Categoria
from authApp.serializers.categoriaSerializer import CategoriaSerializer

class CategoriaDetailView(APIView):
    def get(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404

    def put(self,request, pk=None):
        item = Categoria.objects.get(pk=pk) #obtener item a actualizar
        serializer = CategoriaSerializer(instance=item, data=request.data, partial=True) #Pasar instancia a actualizar y el dato al serializador, partial nos permitirá actualizar sin pasar todo el objeto
        response = Response()
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()

        response.data = {
           'message': 'Category Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, pk):
        item = Categoria.objects.get(pk=pk)
        item.delete()
        
        return Response({
              'message': 'Category Deleted Successfully'
        })