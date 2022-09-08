from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.cita import Cita
from .models.servicio import Servicio
from .models.empleado import Empleado

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Cita)
admin.site.register(Servicio)
admin.site.register(Empleado)