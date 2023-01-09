import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app001 import models
from app001.utils.pagination import pagination

from app001.forms.form_stock import rawstock_Mforms

from app001.utils.bootstrap import BootStrapModelForm


def chart_list(request):
    """数据统计"""
    return render(request, 'chart_list.html')


def chart_bar(request):
    # 柱状图的数据
    legend = ['销量','销量2']
    series_list=[
        {
            "name": '销量',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        },
        {
            "name": '销量2',
            'type': 'bar',
            'data': [123, 20, 362, 120, 120, 202]
        }
    ]
    x_axis =  ['1', '2', '3', '34', '5', '6']

    result = {
        "status":True,
        "data":{
            'legend':legend,
            'series_list':series_list,
            'x_axis':x_axis

        }
    }
    return JsonResponse(result)