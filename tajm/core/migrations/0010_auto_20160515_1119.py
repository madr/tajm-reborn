# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20160515_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absence',
            name='note',
            field=models.TextField(blank=True, default=''),
        ),
    ]