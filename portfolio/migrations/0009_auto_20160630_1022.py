# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20160630_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazon',
            name='x',
            field=models.DateField(),
        ),
    ]
