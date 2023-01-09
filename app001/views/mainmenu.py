from django.shortcuts import render, redirect


def mainmenu(request):
    return render(request, 'mainmenu.html')
