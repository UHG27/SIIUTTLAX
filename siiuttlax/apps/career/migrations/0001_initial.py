# Generated by Django 5.0.6 on 2024-07-15 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_name', models.CharField(max_length=50)),
                ('level', models.CharField(choices=[('TSU', 'Tecnico Suooeriro'), ('Ing', 'Ingenieria'), ('Lic', 'Licenciatura'), ('M', 'Maestria')], max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('plan', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('total_hours', models.IntegerField()),
                ('weekly_hours', models.IntegerField()),
                ('file', models.FileField(blank=True, null=True, upload_to='asignaturas/', verbose_name='Archivo')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career.career')),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
        ),
    ]
