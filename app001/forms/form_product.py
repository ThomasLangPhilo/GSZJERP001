from django import forms
from app001 import models
from django.forms import ValidationError
from app001.utils.bootstrap import BootStrapModelForm


class product_Mforms(BootStrapModelForm):
    # validators = [Regex...]product
    class Meta:
        model = models.product
        # fields = ['product','stocks','industry','stockbase','remark']
        exclude = [ "admin"]





