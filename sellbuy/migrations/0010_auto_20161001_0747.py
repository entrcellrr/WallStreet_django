# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-01 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellbuy', '0009_auto_20160930_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedetail',
            name='money_in_hand',
            field=models.DecimalField(decimal_places=2, default=10000.0, max_digits=14),
        ),
    ]