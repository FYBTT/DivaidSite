# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-04-27 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_auto_20190406_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='specification',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]