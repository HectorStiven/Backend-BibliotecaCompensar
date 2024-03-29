# Generated by Django 4.2.6 on 2023-10-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0019_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=100)),
                ('segundo_nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('primer_apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('numero_celular', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'T002Autores',
            },
        ),
    ]
