# Generated by Django 4.1.1 on 2022-09-13 05:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=20, verbose_name='Apellidos')),
                ('tipoDocumento', models.CharField(max_length=20, verbose_name='Tipo Documento')),
                ('nroDocumento', models.CharField(max_length=15, unique=True, verbose_name='Numero Documento')),
                ('email', models.CharField(max_length=40, verbose_name='Email')),
                ('tipoUsuario', models.CharField(max_length=30, verbose_name='Tipo_Usuario')),
                ('estado', models.CharField(default='Activo', max_length=10, verbose_name='Estado')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=20, verbose_name='Cargo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha Cita')),
                ('hora', models.CharField(max_length=10, verbose_name='Hora')),
                ('lugar', models.CharField(max_length=20, verbose_name='Hora')),
                ('estado', models.CharField(max_length=10, verbose_name='Estado')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_citas_clientes', to='authApp.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_citas_empleado', to='authApp.empleado')),
            ],
        ),
    ]
