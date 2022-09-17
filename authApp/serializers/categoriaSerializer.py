from rest_framework import serializers
from authApp.models import Categoria, Servicio
from .categoriaSerializer import ServicioSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    servicio = ServicioSerializer()
    class Meta:
        model = Categoria
        fields = ['id','nombre','estado','servicio']
    
    def create(self, validated_data):
        servicioData = validated_data.pop('servicio') 
        categoriaInstance = Categoria.objects.create(**validated_data) 
        Servicio.objects.create(categoria=categoriaInstance,**servicioData) 
        return categoriaInstance
    
    def to_representation(self, obj):
        categoria = Categoria.objects.get(id=obj.id) 
        servicio = Servicio.objects.get(categoria=obj.id)
        return{
             'id': categoria.id,
             'nombre': categoria.nombre,
             'estado': categoria.estado,
             'servicio':{
                'id': servicio.id,
                'nombre': servicio.nombre,
                'precio': servicio.precio,
                'estado': servicio.estado
             }
     }