from rest_framework import status, viewsets
from authApp import serializers
from authApp.models import Empleado
from authApp.serializers import EmpleadoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class EmpleadoView(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        serializer = EmpleadoSerializer(self.queryset.order_by("-due_date").filter(owner=9), many=True)
        return Response({'data': serializer.data})

    def retrieve(self, request, pk=None):
        empleado = get_object_or_404(Empleado, id=pk)
        serializer = EmpleadoSerializer(empleado)
        return Response({'data': serializer.data})

    def update(self, request, pk=None):
        empleado = Empleado.objects.get(id=pk)
        serializer = EmpleadoSerializer(empleado, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = EmpleadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        empleado = get_object_or_404(Empleado, id=pk)
        empleado.delete()
        return Response({'status': 'success'})