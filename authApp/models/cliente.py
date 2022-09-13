from django.db import models
from .user import User

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='cliente', on_delete=models.CASCADE)

#on_delete (para mantener integridad referencial de base de datos)