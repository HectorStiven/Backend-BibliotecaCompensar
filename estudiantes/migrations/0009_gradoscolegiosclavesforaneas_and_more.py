# Generated by Django 4.2.6 on 2023-10-27 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0008_remove_grado_jornada'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradosColegiosClavesForaneas',
            fields=[
                ('id_colegio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='estudiantes.colegio')),
                ('id_grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estudiantes.grado')),
            ],
            options={
                'verbose_name': 'Grados Colegios',
                'verbose_name_plural': 'Grados Colegios',
                'db_table': 'T013GradosColegios',
            },
        ),
        migrations.DeleteModel(
            name='TablaConClavesForaneas',
        ),
    ]