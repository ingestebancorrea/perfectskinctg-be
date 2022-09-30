from django.db import models
from .cliente import Cliente
from .empleado import Empleado
from .servicio import Servicio

class Cita(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField('Fecha Cita', auto_now=False,auto_now_add=True)
    hora = models.CharField('Hora', max_length=20)
    lugar = models.CharField('Lugar', max_length=20)
    cliente = models.ForeignKey(Cliente, related_name='fk_citas_clientes', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, related_name='fk_citas_empleados', on_delete=models.CASCADE, null=True)
    servicio = models.ForeignKey(Servicio,related_name='fk_citas_servicios', on_delete=models.CASCADE)
    estado = models.CharField('Estado', max_length=10, default="Agendada")
    