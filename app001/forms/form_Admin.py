from django import forms
from app001 import models
from django.forms import ValidationError
from app001.utils.bootstrap import BootStrapModelForm
from app001.utils.encrypt import md5


class Admin_Mforms(BootStrapModelForm):
    confirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password", ]
        widgets = {
            "password": forms.PasswordInput

        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_Admin(self):
        password = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != password:
            raise ValidationError("密码不一致 ")
        return confirm
