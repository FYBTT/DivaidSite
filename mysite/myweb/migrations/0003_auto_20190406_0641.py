# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-04-06 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0002_remove_specification_goodid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specificationgroupvalue',
            name='specificationId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myweb.Specification'),
        ),
    ]
