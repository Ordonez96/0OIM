# Generated by Django 5.1.2 on 2024-11-01 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoim', '0003_vehiculo_precio_combustible'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='descripcion_corta',
            field=models.TextField(blank=True, null=True),
        ),
    ]
