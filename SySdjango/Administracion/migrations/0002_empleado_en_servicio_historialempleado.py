# Generated by Django 4.2.2 on 2023-08-06 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Administracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='en_servicio',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='HistorialEmpleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ant_nombres', models.CharField(max_length=30)),
                ('ant_apellidos', models.CharField(max_length=30)),
                ('ant_cargo', models.CharField(max_length=100)),
                ('ant_telefono', models.CharField(max_length=20)),
                ('ant_direccion', models.CharField(max_length=200)),
                ('ant_salario', models.FloatField()),
                ('ant_en_servicio', models.BooleanField(default=True)),
                ('act_nombres', models.CharField(max_length=30)),
                ('act_apellidos', models.CharField(max_length=30)),
                ('act_cargo', models.CharField(max_length=100)),
                ('act_telefono', models.CharField(max_length=20)),
                ('act_direccion', models.CharField(max_length=200)),
                ('act_salario', models.FloatField()),
                ('act_en_servicio', models.BooleanField(default=True)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
