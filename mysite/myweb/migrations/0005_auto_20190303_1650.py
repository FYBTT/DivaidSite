# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-03-03 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_auto_20190303_0641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='countrt_text',
            new_name='country_text',
        ),
    ]