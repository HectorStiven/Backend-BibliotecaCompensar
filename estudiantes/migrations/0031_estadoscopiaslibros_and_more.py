# Generated by Django 4.2.6 on 2023-10-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0030_estantes_identificacion_estante_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadosCopiasLibros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Estado de Copia de Libro',
                'verbose_name_plural': 'Estados de Copias de Libros',
                'db_table': 'T024Estados_Copias_Libros',
            },
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion_real',
            field=models.TextField(default='2023-10-27 20:58:28.642645+00:00'),
        ),
    ]
