# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-10 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcels', '0006_auto_20180410_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectortrabajo',
            name='parcela',
        ),
        migrations.AlterField(
            model_name='parcela',
            name='sector_trabajo',
            field=models.ManyToManyField(blank=True, to='parcels.SectorTrabajo'),
        ),
    ]
