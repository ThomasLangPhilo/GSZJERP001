from django.shortcuts import render, redirect
from django.http import JsonResponse

from app001 import models
from app001.utils.pagination import pagination
from django.views.decorators.csrf import csrf_exempt
from app001.forms.form_stockbase import stockbase_Mforms


def stockbase_list(request):
    """仓库列表"""
    #  数据查询
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["contains"] = search_data
    queryset = models.stockbase.objects.all().order_by('-id')
    form = stockbase_Mforms
    page_object = pagination(request, queryset)
    context = {'queryset': page_object.page_queryset,  # 分页的数据
               "page_string": page_object.htme(),  # 分页的页码
               "search_data": search_data,
               'form': form,

               }
    return render(request, 'stockbase_list.html', context)


@csrf_exempt
def stockbase_add(request):
    """新建仓库（AJAX）"""
    form = stockbase_Mforms(data=request.POST)
    if form.is_valid():
        # 当前登录的管理员ID(订单号自动添加管理员ID
        form.instance.admin_id = request.session["info"]['id']
        form.save()

        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def stockbase_detail(request):
    "获取编辑仓库的数据"
    id = request.GET.get('iid')
    row_dict = models.stockbase.objects.filter(id=id).values('stockbasename', 'adress','maxnumber').first()
    if not row_dict:
        return JsonResponse({"status": False, 'error': "不存在数据"})
    # 从数据库获取对象
    result = {
        'status': True,
        'data': row_dict,
    }
    return JsonResponse(result)


@csrf_exempt
def stockbase_edit(request):
    "编辑仓库"

    iid = request.GET.get("iid")
    row_object = models.stockbase.objects.filter(id=iid).first()
    if not row_object:
        return JsonResponse({"status": False, 'tips': "删除失败"})
    form = stockbase_Mforms(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def stockbase_delete(request):
    "删除仓库"

    iid = request.GET.get('iid')
    exists = models.stockbase.objects.filter(id=iid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败"})
    models.stockbase.objects.filter(id=iid).delete()
    return JsonResponse({"status": True})
