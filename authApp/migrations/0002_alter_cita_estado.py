# Generated by Django 4.1.1 on 2022-09-27 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='estado',
            field=models.CharField(default='Agendada', max_length=10, verbose_name='Estado'),
        ),
    ]
