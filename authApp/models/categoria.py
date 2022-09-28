from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=20)
    estado = models.CharField('Estado', max_length=10, default='Activo')