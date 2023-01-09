from django.shortcuts import render, redirect

from app001 import models
from app001.utils.pagination import pagination
from app001.forms.form_Admin import Admin_Mforms


def admin_list(request):
    """管理员列表"""
    #检验有没有登录成功
    info = request.session.get("info")
    if not info:
        return redirect("/login/")
    queryset = models.Admin.objects.all()
    page_object = pagination(request, queryset)
    #
    #  数据查询
    data_dict = {}
    search_data = request.GET.get('q', "")
    if search_data:
        data_dict["contains"] = search_data
    #
    content = {'queryset': queryset,
               'page_string': page_object.htme(),
               "search_data": search_data,

               }
    return render(request, 'admin_list.html', content)



def admin_add(request):
    if request.method == "GET":
        form = Admin_Mforms()
        return render(request, 'changes.html', {"form": form,"title":"管理员添加"})

    form = Admin_Mforms(data=request.POST)
    if form.is_valid():
        #print(form.cleaned_data)
        form.save()
        return redirect('/admin/list/')
    else:
        print((form.errors))
    return render(request, 'changes.html', {"form": form, "title": "管理员添加"})


def admin_edit(request, nid):
    "编辑管理员"
    row_object = models.Admin.objects.filter(id=nid).first()
    if request.method == "GET":
        form = Admin_Mforms(instance=row_object)
        return render(request, 'admin_edit.html', {"form": form})
    form = Admin_Mforms(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'admin_edit.html', {"form": form})


def admin_delete(request, nid):
    "删除管理员"
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')
