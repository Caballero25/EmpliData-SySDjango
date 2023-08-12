# Generated by Django 4.2.2 on 2023-08-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administracion', '0007_alter_datostemporalesnomina_hrs_normales_trabajadas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datostemporalesnomina',
            old_name='hrs_diurnas_trabajadas',
            new_name='hrs_dominical_nocturnas_trabajadas',
        ),
        migrations.AddField(
            model_name='datostemporalesnomina',
            name='hrs_dominical_trabajadas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='datostemporalesnomina',
            name='hrs_normales_trabajadas',
            field=models.IntegerField(default=8),
        ),
    ]