# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20160614_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='contact',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=11),
        ),
    ]
