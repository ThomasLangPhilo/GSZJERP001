from django.shortcuts import render, redirect
from django.http import JsonResponse

from app001 import models
from app001.utils.pagination import pagination
from django.views.decorators.csrf import csrf_exempt
from app001.forms.form_LYKJSYS import LYKJSYS_Mforms_a, LYKJSYS_Mforms_b


#   目前是把数据库的数据打包成字典传到queryset_a和_b(区分借方数据和贷方数据），通过分页函数pagnation变成pageobject对象 打包进context字典传进html中。
def stock2(request):
    """原材料列表"""
    #  数据查询
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["contains"] = search_data
    # 这个是 数据库LYJKSYS借方的数据
    queryset_a = models.LYKJSYS.objects.filter(type_L='1').order_by('-id')
    # 这个是 数据库LYJKSYS贷方的数据
    queryset_b = models.LYKJSYS.objects.filter(type_L='2').order_by('-id')
    # 表单的form
    form_a = LYKJSYS_Mforms_a
    form_b = LYKJSYS_Mforms_b
    page_object_a = pagination(request, queryset_a)
    page_object_b = pagination(request, queryset_b)
    context = {'queryset_a': page_object_a.page_queryset,  # 分页的数据a(借方）
               'queryset_b': page_object_b.page_queryset,  # 分页的数据b（贷方）
               "page_string_a": page_object_a.htme(),  # 分页的页码
               "page_string_b": page_object_b.htme(),  # 分页的页码
               "search_data": search_data,
               'form_a': form_a,
               'form_b': form_b,
               }
    return render(request, 'stock2.html', context)


@csrf_exempt
def stockadd(request):
    """新建原材料（AJAX）"""
    '''将post的数据存放到form中 就是在这里出现问题 本来应该不同的数据放到各自的表单中 但是现在只存放了一个表单的数据到两个form中 应该是识别问题'''
    form_a = LYKJSYS_Mforms_a(data=request.POST)

    form_b = LYKJSYS_Mforms_b(data=request.POST)


    if (form_a.is_valid() and form_b.is_valid()):

        # 当前登录的管理员ID(订单号自动添加管理员ID
        form_a.instance.admin_L_id = request.session["info"]['id']
        form_b.instance.admin_L_id = request.session["info"]['id']
        # 在这里把借和贷的种类传到表单中
        form_a.instance.type_L = '1'
        form_b.instance.type_L = '2'
        # 提交表单到数据库
        form_a.save()
        form_b.save()

        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': (form_a.errors, form_b.errors)})


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
    form = LYKJSYS_Mforms_a(data=request.POST, instance=row_object)
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
