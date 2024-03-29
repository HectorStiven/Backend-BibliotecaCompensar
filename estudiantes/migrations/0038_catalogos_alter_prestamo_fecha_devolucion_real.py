# Generated by Django 4.2.6 on 2023-10-27 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0037_estantes_id_copia_libro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('cantidad_libros_asociados', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Catálogo',
                'verbose_name_plural': 'Catálogos',
                'db_table': 'T027Catalogos',
            },
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion_real',
            field=models.TextField(default='2023-10-27 22:04:33.657525+00:00'),
        ),
    ]
