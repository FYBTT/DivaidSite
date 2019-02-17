# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from .models import Goods, GoodType, Feature
from django.db.models import Q
from django.conf import settings
import json

pageSize = settings.PAGE_SIZE

def home(request):
    context = {}
    return render(request, 'myweb/home.html', context)

def listPage(request, query):
    context = {
        'query': query,
    }
    return render(request, 'myweb/list.html', context)

def listAjaxGet(request, query, page_id):
    start = (int(page_id) - 1)*pageSize
    good_count = Goods.objects.filter(Q(order_no__icontains = query)|Q(typeInShort__icontains = query)).count()
    reSet = Goods.objects.filter(Q(order_no__icontains = query)|Q(typeInShort__icontains = query)).values('order_no', 'typeInShort')[start: pageSize + start]
    print len(reSet)
    result = list(reSet)
    datas = {}
    datas['data'] = result
    datas['totalPages'] = (good_count + pageSize - 1)/pageSize
    return JsonResponse(datas)

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