from django.db import models
from .cliente import Cliente
from .empleado import Empleado

class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha Cita', auto_now=False,auto_now_add=True)
    hora = models.CharField('Hora', max_length=10)
    lugar = models.CharField('Hora', max_length=20)
    cliente = models.ForeignKey(Cliente, related_name='fk_citas_clientes', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, related_name='fk_citas_empleado', on_delete=models.CASCADE)
    estado = models.CharField('Estado', max_length=10)