# Generated by Django 4.2.2 on 2023-08-12 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Administracion', '0005_historialempleado_id_empleado'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='cedula',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DatosTemporalesNomina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_trabajados', models.IntegerField(default=30)),
                ('hrs_normales_trabajadas', models.IntegerField(default=0)),
                ('hrs_nocturnas_trabajadas', models.IntegerField(default=0)),
                ('hrs_diurnas_trabajadas', models.IntegerField(default=0)),
                ('hrs_extras_nocturnas', models.IntegerField(default=0)),
                ('hrs_semanales_contrato', models.IntegerField(default=40)),
                ('hrs_extras_normales', models.IntegerField(default=0)),
                ('pago_mes', models.IntegerField(default=0)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administracion.empleado')),
            ],
        ),
    ]
