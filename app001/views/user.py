from django.shortcuts import render, redirect

from app001.forms.form_Admin import Admin_Mforms


def users_add(request):
    if request.method == "GET":
        form = Admin_Mforms()
        return render(request, 'users_add.html', {"form": form})
    form = Admin_Mforms(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/mainmenu/')
    else:
        print((form.errors))