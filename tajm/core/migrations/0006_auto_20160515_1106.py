# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-15 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160515_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='progress',
            options={'ordering': ['-done_at', 'created_at'], 'verbose_name_plural': 'progresses'},
        ),
        migrations.AddField(
            model_name='progress',
            name='started_at',
            field=models.TimeField(default='00:00:00'),
        ),
    ]