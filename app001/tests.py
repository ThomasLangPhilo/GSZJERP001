from django.test import TestCase

# Create your tests here.
'''
{% extends 'layout.html' %}
{% block content %}
    <div class="container">
        <div>
            <input id="btnAdd" type="button" value="新建订单" class="btn btn-primary">
        </div>


        <div class="panel panel-default">
            <div class="panel-heading">
                订单列表
            </div>
            <!-- Table -->
            <table class="table table-bordered">
                <tr>

                    <th>ID</th>
                    <th>订单号</th>
                    <th>名称</th>
                    <th>价格</th>
                    <th>状态</th>
                    <th>管理员</th>
                    <th>操作</th>
                </tr>

                {% for obj in queryset %}
                    <tr uid="{{ obj.id }}">
                        <td> {{ obj.id }}</td>
                        <td>  {{ obj.oid }}</td>
                        <td> {{ obj.title }}</td>
                        <td> {{ obj.price }}</td>
                        <td> {{ obj.get_status_display }}</td>
                        <td> {{ obj.admin.username }}</td>


                        <td>
                            <a type="submit" class="btn btn-primary" href="#">编辑</a>
                            <input uid="{{ obj.id }}" type="button" class="btn btn-danger  btn-delete" value="删除">
                        </td>
                    </tr>
                {% endfor %}


            </table>
        </div>
        <ul class="pagination">
            {{ page_string }}
        </ul>
    </div>
    <!-- Modal新建订单对话框 -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">新建订单</h4>
                </div>
                <div class="modal-body">
                    <form id="formAdd">
                        <div class="clearfix">
                            {% for field in form %}
                                <div class="col-xs-6">
                                    <div class="form-group" style="position: relative;">
                                        <label> {{ field.label }}:</label>
                                        {{ field }}
                                        <span class="error-msg"
                                              style="color: red;position: absolute;margin-bottom: 20px;"></span>
                                    </div>
                                </div>
                            {% endfor %}

                        </div>


                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                    <button type="button" id="btnSave" class="btn btn-primary">保存</button>
                </div>
            </div>
        </div>

    </div>
    <!-- Modal删除订单对话框 -->

    <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">


                <div class="alert alert-danger alert-dismissible fade in" role="alert">
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                            aria-hidden="true">×</span></button>
                    <h4>是否确定删除</h4>
                    <p style="margin: 10px 0px;">相关数据删除</p>
                    <p style="text-align: right">
                        <button id="btnConfirmDelete" type="button" class="btn btn-danger" data-dismiss="modal">确定</button>
                        <button type="button" class="btn btn-default " data-dismiss="modal">取消</button>
                    </p>
                </div>

        </div>
    </div>
{% endblock %}
{% block js %}
    <script type="text/javascript">
        var DELETE_ID;
        $(function () {
            bindBtnAddEvent();
            btnSaveEvent();
            bindbtnDeleteEvent();
            btnConfirmDelete();
        })

        function bindBtnAddEvent() {
            $("#btnAdd").click(function () {
                $('#myModal').modal('show')
            })
        }

        function btnSaveEvent() {
            $("#btnSave").click(function () {
                //清除错误信息
                $(".error-msg").empty();
                //向后台发送请求

                $.ajax({
                    url: "/order/add/",
                    type: "POST",
                    data: $("#formAdd").serialize(),
                    dataType: "JSON",
                    success: function (res) {
                        if (res.status) {
                            //alert("创建成功");
                            //清空表单
                            $("#formAdd")[0].reset;
                            //关闭对话框
                            $('#myModal').modal('hide');
                            //刷新
                            location.reload();
                        } else {
                            $.each(res.error, function (name, errorList) {
                                $("#id" + name).next().text(errorList[0]);
                            })
                        }
                        console.log(res);
                    }
                })
            })
        }

        function bindbtnDeleteEvent() {
            $(".btn-delete").click(function () {
                // alert("点击了删除")
                $("#deleteModal").modal('show');
                //获取当前的ID并赋值给全部变量
                DELETE_ID = $(this).attr("uid")
            })
        }
        function btnConfirmDelete(){
            $("#btnConfirmDelete").click(function (){
                $.ajax({
                    url:"/order/delete/",
                    type:"GET",
                    data: {
                        uid:DELETE_ID
                    },
                    dataType: "JSON",
                    success:function (res){
                        if(res.status){
                            //删除成功隐藏删除狂
                           // $("#deleteModal").modal('hide');
                            //删除全局变量DELETEID
                            //DELETE_ID=0;
                            //删除当前一行（js）
                            //$("tr[uid='"+DELETE_ID+"']").remove();
                            //



                            //简单的：
                            location.reload();
                        }else {
                            //删除失败
                            alert(res.error())
                        }
                    }
                })
            })
        }
    </script>
{% endblock %}
'''