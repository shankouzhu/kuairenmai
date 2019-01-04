from django.shortcuts import render, redirect
from commend.models import *
from user.common import *
from user.views import checklogin, addusername


# Create your views here.
# 需求发布页面
@checklogin
def demand(request):
    content = {}
    cf = Classification.objects.all()
    content['classobj'] = cf
    return render(request, 'demand/demandnew.html', addusername(content, request))


@checklogin
def publishdemand(request):
    content = {}
    if request.method == "POST":
        title = request.POST.get("zname")
        catagoryid = request.POST.get("industry")
        area = request.POST.get("zname")
        othername = request.POST.get("zname")
        wechar = request.POST.get("zname")
        tel = request.POST.get("zname")
        QQ = request.POST.get("zname")
        endtime = request.POST.get("zname")
        comment = request.POST.get("zname")
        image = request.POST.get("zname")
        money = request.POST.get("zname")

        return render(request, 'demand/demandnew.html', addusername(content, request))
    else:
        return redirect("/user/login/")
