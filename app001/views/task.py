import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app001 import models
from app001.utils.pagination import pagination

from app001.forms.form_stock import rawstock_Mforms

from app001.utils.bootstrap import BootStrapModelForm


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"


def task_list(request):
    """任务列表"""
    form = TaskModelForm
    queryset = models.Task.objects.all().order_by("-id")
    page_object = pagination(request, queryset)
    context = {
        "queryset":page_object.page_queryset,
        "form":form,
        "page_string": page_object.htme(),
    }
    return render(request, 'task_list.html', context)


@csrf_exempt
def task_add(request):
    print(request.POST)

    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, "error": form.errors}
    return HttpResponse(json.dumps(data_dict))
