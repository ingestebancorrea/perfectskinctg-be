from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password= None):
        if not username:
            raise ValueError("Users must have an username")
        
        user = self.model(username=username)
        user.set_password(str(password))
        user.save(using=self._db) 
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        
        user.is_admin = True
        user.save(using=self._db)
        
        return user
           
class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=15, unique=True)
    password = models.CharField('Password', max_length=100)
    nombre = models.CharField('Nombre', max_length=20, null=False)
    apellidos = models.CharField('Apellidos', max_length=20, null=False)
    tipoDocumento = models.CharField('Tipo Documento', max_length=20, null=False)
    nroDocumento = models.CharField('Numero Documento', max_length=15, unique=True)
    email = models.CharField('Email', max_length=40, null=False)
    tipoUsuario = models.CharField("Tipo_Usuario", max_length=30, null=False)
    estado = models.CharField('Estado', max_length=10, default='Activo')
    
    def save(self, **kwargs):
        some_salt = 'qP0nJ7zA8mA4zS4jV5qS8f'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'