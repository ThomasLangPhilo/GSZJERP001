"""ERPGSZJ URL Configuration/-·

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:`
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from app001 import admin
from app001.views import mainmenu, stock, user, admin, account, task, order, chart, product, industry,stockbase,stock2

urlpatterns = [
    # 超级管理员
    # path('admin',admin.)
    # 用户管理
    path('users/add/', user.users_add),
    # 主菜单
    path('mainmenu/', mainmenu.mainmenu),
    # 产品研发
    path('product/list/', product.product_list),
    path('product/add/', product.product_add),
    path('product/edit/', product.product_edit),
    path('product/detail/', product.product_detail),
    path('product/delete/', product.product_delete),
    # 加工厂管理
    path('industry/list/', industry.industry_list),
    path('industry/add/', industry.industry_add),
    path('industry/edit/', industry.industry_edit),
    path('industry/detail/', industry.industry_detail),
    path('industry/delete/', industry.industry_delete),

    # 仓库管理
    path('stockbase/list/', stockbase.stockbase_list),
    path('stockbase/list/', stockbase.stockbase_list),
    path('stockbase/add/', stockbase.stockbase_add),
    path('stockbase/edit/', stockbase.stockbase_edit),
    path('stockbase/detail/', stockbase.stockbase_detail),
    path('stockbase/delete/', stockbase.stockbase_delete),

    # 原材料管理
    path('stock/', stock2.stock2),
    # path('stock/', stock.stock),
    # path('stockadd/', stock.stockadd),
    # path('stock/edit/', stock.stock_edit),
    # path('stock/detail/', stock.stock_detail),
    # path('stock/delete/', stock.stock_delete),
    path('stockadd/', stock2.stockadd),
    path('stock/edit/', stock2.stock_edit),
    path('stock/detail/', stock2.stock_detail),
    path('stock/delete/', stock2.stock_delete),
    # 管理员管理
    path('admin/list/', admin.admin_list),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    # task
    path('task/list/', task.task_list),
    path('task/add/', task.task_add),
    # 订单管理
    path('order/list/', order.order_list),
    path('order/add/', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail/', order.order_detail),
    path('order/edit/', order.order_edit),
    # 数据分析
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
]
