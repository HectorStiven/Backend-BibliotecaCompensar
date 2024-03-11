# Generated by Django 4.2.6 on 2023-10-28 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0043_alter_prestamo_fecha_devolucion_real_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_devolucion_real',
            field=models.TextField(default='2023-10-28 00:33:05.849107+00:00'),
        ),
        migrations.CreateModel(
            name='EstudianteProgramaAcademicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion_semestral', models.CharField(max_length=100)),
                ('id_estudainte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.estudiante')),
                ('id_programa_academico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.programaacademicos')),
            ],
            options={
                'verbose_name': 'Programa Academico',
                'verbose_name_plural': 'Programas Academicos',
                'db_table': 'T008Estudiante_Programas_Academico',
            },
        ),
    ]
