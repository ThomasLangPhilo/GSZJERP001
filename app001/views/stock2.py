from django.shortcuts import render, redirect
from django.http import JsonResponse

from app001 import models
from app001.utils.pagination import pagination
from django.views.decorators.csrf import csrf_exempt
from app001.forms.form_LYKJSYS import LYKJSYS_Mforms


def stock2(request):
    """原材料列表"""
    #  数据查询
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["contains"] = search_data
    queryset = models.LYKJSYS.objects.all().order_by('-id')
    form = LYKJSYS_Mforms
    page_object = pagination(request, queryset)
    context = {'queryset': page_object.page_queryset,  # 分页的数据
               "page_string": page_object.htme(),  # 分页的页码
               "search_data": search_data,
               'form': form,
               }
    return render(request, 'stock2.html', context)


@csrf_exempt
def stockadd(request):
    """新建原材料（AJAX）"""
    form = LYKJSYS_Mforms(data=request.POST)
    if form.is_valid():
        # 当前登录的管理员ID(订单号自动添加管理员ID
        form.instance.admin_L_id = request.session["info"]['id']
        form.save()

        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})

def stock_detail(request):
    "获取编辑原材料的数据"
    stockid = request.GET.get('stockid')
    row_dict = models.LYKJSYS.objects.filter(id=stockid).values().first()
    if not row_dict:
        return JsonResponse({"status": False, 'error': "不存在数据"})
    # 从数据库获取对象
    result = {
        'status': True,
        'data': row_dict,
    }
    return JsonResponse(result)


@csrf_exempt
def stock_edit(request):
    "编辑原材料"
    # row_object = models.rawstock.objects.filter(id=nid).first()
    # if request.method == "GET":
    #     form = rawstock_Mforms(instance=row_object)
    #     return render(request, 'stock_edit.html', {"form": form})
    # form = rawstock_Mforms(data=request.POST, instance=row_object)
    # if form.is_valid():
    #     form.save()
    #     return redirect('/stock/')
    # return render(request, 'stock_edit.html', {"form": form})
    stockid = request.GET.get("stockid")
    row_object = models.LYKJSYS.objects.filter(id=stockid).first()
    if not row_object:
        return JsonResponse({"status": False, 'tips': "删除失败"})
    form = LYKJSYS_Mforms(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def stock_delete(request):
    "删除原材料"
    # models.rawstock.objects.filter(id=nid).delete()
    # return redirect('/stock/')
    stockid = request.GET.get('stockid')
    exists = models.LYKJSYS.objects.filter(id=stockid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败"})
    models.LYKJSYS.objects.filter(id=stockid).delete()
    return JsonResponse({"status": True})
