# Generated by Django 5.1.1 on 2024-10-13 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='crearContrasena',
            new_name='contrasena',
        ),
    ]
