from django.shortcuts import render, HttpResponse,redirect
from django import forms
from app001 import models
from app001.utils.bootstrap import BootStrapForm
from app001.utils.encrypt import md5
class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        required=True
    )

    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput,
        required=True

    )

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
        #return pwd


def login(request):
    '''登录'''
    if request.method == 'GET':
        forms = LoginForm()
        return render(request, 'login.html', {"form": forms})

    forms = LoginForm(data=request.POST)
    if forms.is_valid():
        # 检验数据库的数据
        admin_object = models.Admin.objects.filter(**forms.cleaned_data).first()
        if not admin_object:
            forms.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": forms})
        # 用户名或密码正确
        #return HttpResponse("1")
        # 生成随机字符串写进cookie中再写入session中
        request.session["info"] ={'id':admin_object.id,'name':admin_object.username }
        return redirect('/admin/list')
    return render(request, 'login.html', {"form": forms})


def logout(request):
    """注销"""
    request.session.clear()
    return redirect("/login/")
