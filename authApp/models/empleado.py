from django.db import models
from .user import User

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='empleados', on_delete=models.CASCADE)
    cargo = models.CharField('Cargo', max_length=20)
    nombre = models.CharField('Nombre', max_length=20)
    apellidos = models.CharField('Apellidos', max_length=20)
    tipoDocumento = models.CharField('Tipo Documento', max_length=20)
    nroDocumento = models.CharField('Numero Documento', max_length=15, unique=True)
    sexo = models.CharField('Sexo', max_length=10)
    telefono = models.CharField('Telefono', max_length=15)
    email = models.CharField('Email', max_length=20)
    direccion = models.CharField('Direccion', max_length=40)
    estado = models.CharField('Estado', max_length=10)