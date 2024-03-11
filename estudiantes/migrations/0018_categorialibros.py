# Generated by Django 4.2.6 on 2023-10-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0017_alter_bandejaentrante_table_alter_estantes_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaLibros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=100)),
                ('otra_categoria_cual', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Categoría de Libros',
                'verbose_name_plural': 'Categorías de Libros',
                'db_table': 'T004CategoriaLibros',
            },
        ),
    ]