# Generated by Django 4.1.1 on 2022-09-17 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_categoria_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Precio'),
        ),
    ]
