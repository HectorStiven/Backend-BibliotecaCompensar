# Generated by Django 5.0.3 on 2024-04-12 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_usuario_alter_prestamo_fecha_devolucion_real_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion_real',
            field=models.TextField(default='2024-04-12 01:52:09.104084+00:00'),
        ),
    ]
