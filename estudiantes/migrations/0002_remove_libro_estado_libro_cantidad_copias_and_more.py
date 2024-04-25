# Generated by Django 5.0.3 on 2024-04-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='estado',
        ),
        migrations.AddField(
            model_name='libro',
            name='cantidad_copias',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='libro',
            name='estado_libro',
            field=models.BooleanField(default=True),
        ),
    ]
