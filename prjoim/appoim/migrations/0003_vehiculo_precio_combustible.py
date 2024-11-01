# Generated by Django 5.1.2 on 2024-11-01 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoim', '0002_rename_gasto_combustible_por_km_vehiculo_km_por_galon'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='precio_combustible',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
    ]