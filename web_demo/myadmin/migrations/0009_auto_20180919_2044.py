# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-19 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0008_auto_20180919_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]