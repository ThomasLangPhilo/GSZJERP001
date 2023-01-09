from django import forms
from app001 import models
from django.forms import ValidationError
from app001.utils.bootstrap import BootStrapModelForm


class rawstock_Mforms(BootStrapModelForm):
    # validators = [Regex...]
    class Meta:
        model = models.rawstock
        exclude = ['admin']


    def clean_stock(self):
        print(self.instance.pk)
        txt_rawstock = self.cleaned_data["rawstock"]
        exists = models.rawstock.objects.exclude(id=self.instance.pk).filter(name=txt_rawstock).exists()
        if exists:
            raise ValidationError("已存在名称")
        return txt_rawstock


