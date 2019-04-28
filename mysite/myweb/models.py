# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Feature(models.Model):
    fea_text = models.CharField(max_length = 300)
    def __str__(self):
        return self.fea_text

class GoodType(models.Model):
    type_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.type_text

class Goods(models.Model):
    order_no = models.CharField(max_length = 30)
    features = models.ManyToManyField(Feature)
    typeInShort = models.CharField(max_length = 30, default = 'Regulator')
    type_no = models.ForeignKey(GoodType, on_delete = models.CASCADE)
    country_no = models.CharField(max_length = 5, default = '00')
    def __str__(self):
        return self.order_no

class Country(models.Model):
    country_no = models.CharField(primary_key = True, max_length = 5)
    country_text = models.CharField(max_length = 50)
    def __str__(self):
        return self.country_text

class Specification(models.Model):
    specification_text = models.CharField(max_length = 100)
    weight = models.IntegerField(default = 0)
    def __str__(self):
        return self.specification_text

class SpecificationGroupValue(models.Model):
    goodId = models.IntegerField(default = 0)
    specificationId = models.ForeignKey(Specification, on_delete = models.CASCADE)
    valueIndex = models.IntegerField(default = 0)
    value = models.CharField(max_length = 300)
    def __str__(self):
        return str(self.goodId)
