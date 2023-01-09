'''
        自定义的分类组件
    筛选数据
    queryset = models.rawstock.objects.all()
    实例化分页对象
    page_object = pagination(request,queryset)

    context = {'queryset': page_object.page_queryset,#分页的数据
               "page_string": page_object.htme(),#分页的页码
               "search_data":search_data,

               }
    return render(request, 'stock.html', context)
    在html中
    {% for item in queryset %}
                <tr>
                    <td> {{ item.name }}</td>
                    <td>  {{ item.number }}</td>
                    <td> {{ item.amount }}</td>
                    <td> {{ item.price }}</td>
                    <td>  {{ item.remark }}</td>
                    <td>
                        <a type="submit" class="btn btn-primary" href="../stock/{{ item.id }}/edit/">编辑</a>
                    </td>
                    <td>
                        <a type="submit" class="btn btn-warning" href="../stock/{{ item.id }}/delete/">删除</a>
                    </td>
                </tr>
            {% endfor %}
    <ul class="pagination">
            {{ page_string }}
    </ul>
'''

from django.utils.safestring import mark_safe


class pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5, ):
        """


        :param request: 请求的对象
        :param queryset:符合条件的数据（进行分页处理）
        :param page_size:每页显示多少条数据
        :param page_param:在url中传递的参数
        :param plus:显示当前页码（前后）
        """
        from django.http.request import QueryDict
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param
        page = (request.GET.get(page_param, "1"))
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        # 数据总共条数
        total_count = queryset.count()
        # 总页码
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    def htme(self):

        # 显示当前前5-后5页
        self.plus = 5
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                if (self.page + self.plus) > self.total_page_count:
                    end_page = self.total_page_count
                    start_page = self.total_page_count - 2 * self.plus
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus + 1
        # 页码
        page_str_list = []
        self.query_dict.setlist(self.page_param, [1])
        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href=?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)
        # 页面

        for i in range(start_page, end_page):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:

                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)

            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)
        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])

            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        search_string = """<li>
                    <form method="get" style="float:left;margin-left:-1px">

                        <input
                                type="text"
                                name="page"
                                style="position: relative;float: left;display: inline-block;width: 80px;border-radius: 0;"
                                class="form-control "
                                placeholder="页码">

                        <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
                    </form>


                </li>"""
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string
