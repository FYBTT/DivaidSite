# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Goods, GoodType, Feature

admin.site.register(Goods)
admin.site.register(GoodType)
admin.site.register(Feature)