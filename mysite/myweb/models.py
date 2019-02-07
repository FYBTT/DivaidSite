# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Feature(models.Model):
    fea_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.fea_text

class GoodType(models.Model):
    type_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.type_text

class Goods(models.Model):
    order_no = models.CharField(max_length = 30)
    gas = models.CharField(max_length = 20)
    max_inlet_pressure = models.FloatField(default = 0)
    max_outlet_pressure = models.FloatField(default = 0)
    inlet_connection = models.CharField(max_length = 10)
    outlet_connection = models.CharField(max_length = 20)
    features = models.ManyToManyField(Feature)
    type_no = models.ForeignKey(GoodType, on_delete = models.CASCADE)
    def __str__(self):
        return self.order_no