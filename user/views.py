from django.shortcuts import render, HttpResponse, redirect
from user.models import Userinfo
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def login_handler(request):
    resp = {'status': 400, 'data': 'login fail'}
    if request.method == "POST":
        usernm = request.POST.get("username")
        passwd = request.POST.get("password")
        print(usernm, passwd)
        # Userinfo.objects.get(username=phone)
        resp
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        return HttpResponse(json.dumps(resp), content_type="application/json")


def register(request):
    return render(request, 'register.html')
