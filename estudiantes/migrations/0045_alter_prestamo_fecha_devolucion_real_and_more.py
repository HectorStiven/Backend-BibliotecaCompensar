# Generated by Django 4.2.6 on 2023-10-28 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0044_alter_prestamo_fecha_devolucion_real_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion_real',
            field=models.TextField(default='2023-10-28 01:29:26.243633+00:00'),
        ),
        migrations.AlterModelTable(
            name='catalogoslibros',
            table='T028CatalogosLibros',
        ),
    ]
