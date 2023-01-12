from django.db import models


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class users(models.Model):
    """用户"""
    name = models.CharField(max_length=16, verbose_name="名称")
    password = models.CharField(max_length=32, verbose_name="密码")
    gender_choices = (
        (1, "man"),
        (2, "women")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)


class account_t(models.Model):
    "科目表"
    name_a = models.CharField(max_length=64)
    def __str__(self):
        return self.name_a

class rawstock(models.Model):
    "原材料库存"

    name = models.CharField(verbose_name="原料", max_length=32, default=None)
    remark = models.CharField(verbose_name="备注", max_length=32, default=None, )
    number = models.SmallIntegerField(verbose_name="编号", default=None, )
    amount = models.SmallIntegerField(verbose_name="数量", default=None, )
    price = models.SmallIntegerField(verbose_name="单价", default=None, )
    admin = models.ForeignKey(verbose_name="管理员", to=Admin, on_delete=models.CASCADE, )

    def __str__(self):
        return self.name
    # 无约束
    # depart_id = models.BigIntegerField()
    # 有约束 to 是与那张表关联 to_field——与那一列关联 on_delete=models.CASCADE级联删除
    # depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.CASCADE)
    # 允许为空 与级联删除相反


# depart = models.ForeignKey(to="Department", to_fields="id", on_delete=models.SET_NULL(), null=True, blank=True, )


class Task(models.Model):
    "任务"
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),

    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=3)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="备注", max_length=64)
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)


class industry(models.Model):
    """加工厂"""

    industryname = models.CharField(verbose_name="工厂名称", max_length=64)
    adress = models.CharField(verbose_name="地址", max_length=128)

    def __str__(self):
        return self.industryname


class stockbase(models.Model):
    """仓库"""

    stockbasename = models.CharField(verbose_name="仓库名称", max_length=64, )
    adress = models.CharField(verbose_name="仓库地址", max_length=128, )
    maxnumber = models.SmallIntegerField(verbose_name="容纳数量", )

    def __str__(self):
        return self.stockbasename


class product(models.Model):
    """产品研发的数据库"""
    product = models.CharField(verbose_name="产品名称", max_length=64)
    stocks = models.ForeignKey(verbose_name="原材料", to=rawstock, on_delete=models.CASCADE, )
    industry = models.ForeignKey(verbose_name="工厂", to=industry, on_delete=models.CASCADE)
    stockbase = models.ForeignKey(verbose_name="仓库", to=stockbase, on_delete=models.CASCADE)
    remark = models.CharField(verbose_name="备注", max_length=32, default=None, null=True)
    admin = models.ForeignKey(verbose_name="管理员", to=Admin, on_delete=models.CASCADE, )


class Order(models.Model):
    """订单"""
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    status_choices = {
        (1, "待支付"),
        (2, "已支付"),
    }
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    admin = models.ForeignKey(verbose_name="管理员", to=Admin, on_delete=models.CASCADE)


class LYKJSYS(models.Model):
    '''LYKJSYS郎岩会计系统的数据库'''
    typt_L_choices = (
        (1, "借"),
        (2, "贷"),
        (3, "待处理"),
    )
    kemu_L = models.ForeignKey(verbose_name="会计科目", to=account_t, on_delete=models.CASCADE)
    zijin_L = models.SmallIntegerField(verbose_name='资金数量', default=0)
    time_L = models.TimeField(verbose_name='时间',null=True,blank=True)
    number_L = models.CharField(verbose_name='编号',max_length=64,null=True,blank=True)
    type_L = models.SmallIntegerField(verbose_name='借/贷', choices=typt_L_choices, )
    admin_L = models.ForeignKey(verbose_name='管理员', to=Admin, on_delete=models.CASCADE)
    note_L = models.CharField(verbose_name='备注',null=True,max_length=64,blank=True)