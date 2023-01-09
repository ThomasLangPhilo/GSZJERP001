from django.shortcuts import render, redirect
from django.http import JsonResponse

from app001 import models
from app001.utils.pagination import pagination
from django.views.decorators.csrf import csrf_exempt
from app001.forms.form_industry import industry_Mforms


def industry_list(request):
    """工厂列表"""
    #  数据查询
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["contains"] = search_data
    queryset = models.industry.objects.all()
    form = industry_Mforms
    page_object = pagination(request, queryset)
    context = {'queryset': page_object.page_queryset,  # 分页的数据
               "page_string": page_object.htme(),  # 分页的页码
               "search_data": search_data,
               'form': form,

               }
    return render(request, 'industry_list.html', context)


@csrf_exempt
def industry_add(request):
    """新建工厂（AJAX）"""
    form = industry_Mforms(data=request.POST)
    if form.is_valid():
        # 当前登录的管理员ID(订单号自动添加管理员ID
        form.instance.admin_id = request.session["info"]['id']
        form.save()

        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def industry_detail(request):
    "获取编辑工厂的数据"
    id = request.GET.get('iid')
    row_dict = models.industry.objects.filter(id=id).values('industryname', 'adress').first()
    if not row_dict:
        return JsonResponse({"status": False, 'error': "不存在数据"})
    # 从数据库获取对象
    result = {
        'status': True,
        'data': row_dict,
    }
    return JsonResponse(result)


@csrf_exempt
def industry_edit(request):
    "编辑工厂"

    iid = request.GET.get("iid")
    row_object = models.industry.objects.filter(id=iid).first()
    if not row_object:
        return JsonResponse({"status": False, 'tips': "删除失败"})
    form = industry_Mforms(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def industry_delete(request):
    "删除工厂"

    iid = request.GET.get('iid')
    exists = models.industry.objects.filter(id=iid).exists()
    if not exists:
        return JsonResponse({"status": False, 'error': "删除失败"})
    models.industry.objects.filter(id=iid).delete()
    return JsonResponse({"status": True})
