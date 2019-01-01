from django.shortcuts import render, HttpResponse, redirect
from user.models import Userinfo

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def login_handler(request):
    if request.method == "POST":
        phone=request.POST.get("phone")
        passwd=request.POST.get("pass")
        Userinfo.objects.get(username=phone)
    else:
        return redirect('/user/login/')


def register(request):
    return render(request, 'register.html')
