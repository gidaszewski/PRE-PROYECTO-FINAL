# Generated by Django 3.0.1 on 2022-11-14 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_auto_20221114_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inscripcion',
            old_name='apellido',
            new_name='password',
        ),
    ]
