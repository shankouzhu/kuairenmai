from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Userinfo
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def login_handler(request):
    resp = {'status': 400, 'data': '登录失败'}
    if request.method == "POST":
        usernm = request.POST.get("username")
        passwd = request.POST.get("password")
        user = Userinfo.objects.get(username=usernm)
        if user:
            if passwd == user.password:
                request.session['username'] = usernm
                resp['status'] = 200
                resp['data'] = 'success'
            else:
                resp['data'] = '密码错误'
        else:
            resp['data'] = '用户不存在'
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        return HttpResponse(json.dumps(resp), content_type="application/json")


def register(request):
    return render(request, 'register.html')
