from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect
class AuthMiddleware(MiddlewareMixin):
    """中间件1"""
    def process_request(self,request):
        #排除不需要验证登录的界面
        if request.path_info == "/login/":
            return
        #读取当前用户session信息 读到说明已经登陆过
        info_dict = request.session.get("info")
        if info_dict:
            return
        #没有登陆过：
        return redirect("/login/")