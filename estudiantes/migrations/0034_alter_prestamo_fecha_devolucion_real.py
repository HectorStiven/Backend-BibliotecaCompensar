# Generated by Django 4.2.6 on 2023-10-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0033_alter_prestamo_fecha_devolucion_real'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion_real',
            field=models.TextField(default='2023-10-27 21:45:40.473127+00:00'),
        ),
    ]