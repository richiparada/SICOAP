# Generated by Django 3.2.25 on 2024-07-22 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_bodega'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bodega',
            old_name='nombreResponsable',
            new_name='nombre_responsable',
        ),
    ]
