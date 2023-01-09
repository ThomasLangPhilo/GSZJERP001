from django import forms
from app001 import models
from django.forms import ValidationError
from app001.utils.bootstrap import BootStrapModelForm


class stockbase_Mforms(BootStrapModelForm):
    # validators = [Regex...]product
    class Meta:
        model = models.stockbase
        # fields = ['product','stocks','industry','stockbase','remark']
        fields = '__all__'




