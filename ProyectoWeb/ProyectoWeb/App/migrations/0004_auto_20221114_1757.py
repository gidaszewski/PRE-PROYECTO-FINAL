# Generated by Django 3.0.1 on 2022-11-14 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20221114_1730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscripcion',
            old_name='password',
            new_name='contraseña',
        ),
    ]
