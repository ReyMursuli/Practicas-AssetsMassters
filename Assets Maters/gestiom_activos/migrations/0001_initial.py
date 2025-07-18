# Generated by Django 5.1.4 on 2025-06-30 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('codigo', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_interno', models.CharField(max_length=50, unique=True)),
                ('rotulo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('valor_inicial', models.DecimalField(decimal_places=2, max_digits=12)),
                ('valor_residual', models.DecimalField(decimal_places=2, max_digits=12)),
                ('depen_acomulada', models.DecimalField(decimal_places=2, max_digits=12)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qrcodes')),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='activos_asignados', to='usuarios.responsable')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activos', to='gestiom_activos.area')),
            ],
        ),
    ]
