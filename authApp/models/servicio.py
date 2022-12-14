from django.db import models
from authApp.models.categoria import Categoria

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, related_name='fk_servicios_categorias', on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=20)
    precio = models.DecimalField('Precio', max_digits = 19, decimal_places = 2)
    estado = models.CharField('Estado', max_length=10, default='Activo')