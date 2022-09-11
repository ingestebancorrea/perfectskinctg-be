from django.db import models
from .user import User

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='cliente', on_delete=models.CASCADE)
    nombre = models.CharField('Nombre', max_length=20)
    apellidos = models.CharField('Apellidos', max_length=20)
    tipoDocumento = models.CharField('Tipo Documento', max_length=20)
    nroDocumento = models.CharField('Numero Documento', max_length=15, unique=True)
    sexo = models.CharField('Sexo', max_length=10)
    telefono = models.CharField('Telefono', max_length=15)
    email = models.CharField('Email', max_length=40)
    direccion = models.TextField()
    estado = models.CharField('Estado', max_length=10)

#on_delete (para mantener integridad referencial de base de datos)