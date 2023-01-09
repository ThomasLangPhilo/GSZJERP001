from django import forms
from app001 import models
from django.forms import ValidationError
from app001.utils.bootstrap import BootStrapModelForm


class industry_Mforms(BootStrapModelForm):
    # validators = [Regex...]product
    class Meta:
        model = models.industry
        # fields = ['product','stocks','industry','stockbase','remark']
        fields = '__all__'