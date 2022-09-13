from django.db import models
from .user import User

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='empleados', on_delete=models.CASCADE)
    cargo = models.CharField('Cargo', max_length=20)