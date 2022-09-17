from authApp.models import Servicio, Categoria
from rest_framework import serializers
from .categoriaSerializer import CategoriaSerializer

class ServicioSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    class Meta:
        model = Servicio
        fields = ['id', 'nombre', 'precio', 'stock', 'estado', 'categoria']
    
    def create(self, validated_data):
        categoriaData = validated_data.pop('categoria') 
        servicioInstance = Servicio.objects.create(**validated_data) 
        Categoria.objects.create(servicio=servicioInstance,**categoriaData) 
        return servicioInstance
    
    def to_representation(self, obj):
        servicio = Servicio.objects.get(id=obj.id)
        categoria = Categoria.objects.get(servicio=obj.id) 
        return{
             'id': servicio.id,
             'nombre': servicio.nombre,
             'precio': servicio.precio,
             'stock': servicio.stock,
             'estado': servicio.estado,
             'categoria':{
                'id': categoria.id,
                'nombre': categoria.nombre,
                'estado': categoria.estado
             }
     }