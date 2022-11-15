# Generated by Django 3.0.1 on 2022-11-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lanzamientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_lanzamiento', models.CharField(max_length=40)),
                ('fecha_de_lanzamiento', models.DateField()),
                ('incluye', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('nacionalidad', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Presentaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_fiesta', models.CharField(max_length=40)),
                ('fecha_fiesta', models.DateField()),
                ('artistas', models.CharField(max_length=40)),
            ],
        ),
    ]
