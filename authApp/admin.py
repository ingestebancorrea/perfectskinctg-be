from django.contrib import admin
from .models.user import User
from .models.cita import Cita
from .models.cliente import Cliente
from .models.empleado import Empleado

# Registrarlo dentro de admin:
admin.site.register(User)
admin.site.register(Cita)
admin.site.register(Cliente)
admin.site.register(Empleado)
