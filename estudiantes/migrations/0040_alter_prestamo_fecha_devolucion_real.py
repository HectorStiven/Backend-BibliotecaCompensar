# Generated by Django 4.2.6 on 2023-10-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0039_alter_prestamo_fecha_devolucion_real_catalogoslibros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion_real',
            field=models.TextField(default='2023-10-27 23:20:19.219763+00:00'),
        ),
    ]