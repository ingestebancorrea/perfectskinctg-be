from rest_framework import status, viewsets
from authApp import serializers
from authApp.models import Cita
from authApp.serializers import CitaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CitaView(viewsets.ModelViewSet):
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        serializer = CitaSerializer(self.queryset.order_by("fecha").filter(cliente=1), many=True)
        return Response({'data': serializer.data})

    def retrieve(self, request, pk=None):
       cita = get_object_or_404(Cita, id=pk)
       serializer = CitaSerializer(cita)
       return Response({'data': serializer.data})

    def update(self, request, pk=None):
        cita = Cita.objects.get(id=pk)
        serializer = CitaSerializer(cita, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = CitaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        cita = get_object_or_404(Cita, id=pk)
        cita.delete()
        return Response({'status': 'success'})