# Generated by Django 5.2.4 on 2025-08-01 22:49

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0006_capitulo_dias_disponibles'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemaBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CapituloBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo_entrega', models.CharField(blank=True, choices=[('', 'Seleccionar'), ('ondemand', 'On Demand'), ('envivo', 'En Vivo')], default='', max_length=20, null=True)),
                ('tipo_contenido', models.CharField(blank=True, choices=[('', 'Seleccionar'), ('masterclass', 'Masterclass'), ('curso', 'Curso')], default='', max_length=20, null=True)),
                ('dias_disponibles', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miércoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sábado'), ('domingo', 'Domingo')], max_length=52, null=True)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capitulos_business', to='packages.temabusiness')),
            ],
        ),
    ]
