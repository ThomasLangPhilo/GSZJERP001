from django import forms

class BootStrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环每一个字段 给每个字段插件设置
        for name, field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label

            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class BootStrapModelForm(BootStrap,forms.ModelForm):
    pass



class BootStrapForm(BootStrap,forms.Form):
    pass
