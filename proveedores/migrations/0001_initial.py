# Generated by Django 3.2.25 on 2024-07-22 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=12)),
                ('placa_patente', models.CharField(max_length=10)),
                ('empresa', models.CharField(max_length=100)),
                ('numero_contacto', models.CharField(max_length=15)),
            ],
        ),
    ]
