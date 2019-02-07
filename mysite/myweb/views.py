# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from .models import Goods, GoodType, Feature

def home(request):
    context = {}
    return render(request, 'myweb/home.html', context)

def search(request):
    if 'good' in request.GET:
        good_id = request.GET['good']
        reSet = Goods.objects.filter(order_no__icontains = good_id)
        print len(reSet)
        if len(reSet) > 1:
            return HttpResponse("hello list ")
        else:
            return good(request, good_id)
    else:
        return HttpResponse("no good info")

def listGet(request, page_id):
    goodsList = Goods.objects.all()
    output = ','.join([q.gas for q in goodsList])
    return HttpResponse("hello list " + output)

def good(request, good_id):
    reSet = Goods.objects.filter(order_no = good_id)
    reGood = reSet[0]
    feaList = reGood.features.all()
    features = []
    for fea in feaList:
        features.append(fea.fea_text)
    pic = reGood.order_no.split('-')[-1]
    pic = pic + ".jpg"
    print pic
    context = {
        'typeName': reGood.type_no.type_text,
        'feature': features,
        'good': reGood,
        'pic': pic,
    }
    return render(request, 'myweb/detail.html', context)