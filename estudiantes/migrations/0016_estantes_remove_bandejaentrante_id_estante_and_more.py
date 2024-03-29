# Generated by Django 4.2.6 on 2023-10-27 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0015_bandejaentrante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estantes',
            fields=[
                ('id_estante', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('id_Libro', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Estante',
                'verbose_name_plural': 'Estantes',
                'db_table': 't021Estantes',
            },
        ),
        migrations.RemoveField(
            model_name='bandejaentrante',
            name='id_estante',
        ),
        migrations.AddField(
            model_name='bandejaentrante',
            name='estante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='estudiantes.estantes'),
        ),
    ]
