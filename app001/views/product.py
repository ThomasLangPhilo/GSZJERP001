from django.shortcuts import render, redirect
from django.http import JsonResponse

from app001 import models
from app001.utils.pagination import pagination
from django.views.decorators.csrf import csrf_exempt
from app001.forms.form_product import product_Mforms


def product_list(request):
    """产品列表"""
    #  数据查询
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["contains"] = search_data
    queryset = models.product.objects.filter().all().order_by("-id")
    product_form = product_Mforms
    page_object = pagination(request, queryset)
    context = {'queryset': page_object.page_queryset,  # 分页的数据
               "page_string": page_object.htme(),  # 分页的页码
               "search_data": search_data,
               'form': product_form,
               }
    return render(request, 'product_list.html', context)


@csrf_exempt
def product_add(request):
    """新建产品（AJAX）"""
    form = product_Mforms(data=request.POST)
    # 当前登录的管理员ID(订单号自动添加管理员ID
    form.instance.admin_id = request.session["info"]['id']
    if form.is_valid():
        form.save()

        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def product_detail(request):
    "获取编辑原材料的数据"
    pid = request.GET.get('pid')
    row_dict = models.product.objects.filter(id=pid).values("product", "remark", "stocks", "industry",
                                                            "stockbase", ).first()
    if not row_dict:
        return JsonResponse({"status": False, 'error': "不存在数据"})
    # 从数据库获取对象
    result = {
        'status': True,
        'data': row_dict,
    }
    return JsonResponse(result)


@csrf_exempt
def product_edit(request):
    "编辑产品"

    pid = request.GET.get("pid")
    row_object = models.product.objects.filter(id=pid).first()
    if not row_object:
        return JsonResponse({"status": False, 'tips': "删除失败"})
    form = product_Mforms(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def product_delete(request):
    " 删除产品 "
    pid = request.GET.get('pid')
    exists = models.product.objects.filter(id=pid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败"})
    models.product.objects.filter(id=pid).delete()
    return JsonResponse({"status": True})
