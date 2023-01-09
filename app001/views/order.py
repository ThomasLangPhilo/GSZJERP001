import random
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from app001 import models
from app001.utils.bootstrap import BootStrapModelForm
from app001.utils.pagination import pagination


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        exclude = ["oid", "admin"]


def order_list(request):
    queryset = models.Order.objects.all().order_by('-id')
    form = OrderModelForm
    page_object = pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "form": form,
        "page_string": page_object.htme(),
    }

    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """新建订单（AJAX）"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # 额外生成OID(订单号）
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))

        # 当前登录的管理员ID(订单号自动添加管理员ID
        form.instance.admin_id = request.session["info"]['id']

        form.save()

        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def order_delete(request):
    """删除订单"""
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败"})
    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_detail(request):
    '''获取订单详细'''
    uid = request.GET.get('uid')
    row_dict = models.Order.objects.filter(id=uid).values('title', 'price', 'status').first()
    if not row_dict:
        return JsonResponse({"status": False, 'error': "不存在数据"})
    # 从数据库获取对象
    result = {
        'status': True,
        'data': row_dict,
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    '''订单编辑'''
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, 'tips': "删除失败"})
    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})
