# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from .models import Goods, GoodType, Feature, Country, SpecificationGroupValue, Specification
from django.db.models import Q
from django.conf import settings
import json

pageSize = settings.PAGE_SIZE

def home(request):
    context = {}
    return render(request, 'myweb/home.html', context)

def listPage(request, country, query):
    re = Country.objects.all()
    context = {
        'query': query,
        'country': re,
        'selectCountry': country,
    }
    return render(request, 'myweb/list.html', context)

def listAjaxGet(request, query, country, page_id):
    start = (int(page_id) - 1)*pageSize
    if country == '000':
        good_count = Goods.objects.filter(Q(order_no__icontains = query)|Q(typeInShort__icontains = query)).count()
        reSet = Goods.objects.filter(Q(order_no__icontains = query)|Q(typeInShort__icontains = query)).values('order_no', 'typeInShort')[start: pageSize + start]    
    else:    
        good_count = Goods.objects.filter(country_no = country).filter(Q(order_no__icontains = query)|Q(typeInShort__icontains = query)).count()
        reSet = Goods.objects.filter(country_no = country).filter(Q(order_no__icontains = query)|Q(typeInShort__icontains = query)).values('order_no', 'typeInShort')[start: pageSize + start]
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
    #pic = reGood.order_no.split('-')[-1]
    pic = reGood.order_no + ".jpg"
    specificationItems = SpecificationGroupValue.objects.filter(goodId = reGood.id)
    header = []
    lines = []
    re = specificationItems.filter(valueIndex = 0)
    if len(re) > 0:
        line = []
        for spe in re:
            des = spe.specificationId.specification_text
            header.append(des)
            line.append(spe.value)
        lines.append(line)
        for i in xrange(1, len(specificationItems)):
            re = specificationItems.filter(valueIndex = i)
            if len(re) == 0:
                break
            line = []
            for spe in re:
                line.append(spe.value)
            lines.append(line)
    context = {
        'pic': pic,
        'order_no': reGood.order_no,
        'typeName': reGood.type_no.type_text,
        'typeInShort': reGood.typeInShort,
        'feature': features,
        'header':header,
        'specificationItem': lines,
    }
    print lines
    return render(request, 'myweb/detail.html', context)

def page_not_found(request):
    context = {}
    return render(request, 'myweb/404.html', context)