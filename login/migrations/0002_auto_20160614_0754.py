# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='id',
            field=models.PositiveSmallIntegerField(primary_key='True', serialize=False),
        ),
    ]