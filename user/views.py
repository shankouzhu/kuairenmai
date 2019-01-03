from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Userinfo
from user import common
from io import BytesIO
import json


# Create your views here.
# 装饰器检查是否登录
def checklogin(myfunc):
    def check(request, *args, **kwargs):
        if request.session.get('username'):
            return myfunc(request, *args, **kwargs)
        else:
            return redirect("/user/login/")

    return check


# 主页
def index(request):
    # 获取用户账户
    username = request.session.get('username') if request.session.get('username') else None
    return render(request, 'index.html', {'username': username})


# 登录
def login(request):
    return render(request, 'login.html')


# 注销
@checklogin
def dellogin(request):
    del request.session['username']
    return redirect('/user/login/')


# 登录逻辑处理
def login_handler(request):
    # 信息
    resp = {'status': 400, 'data': '登录失败'}
    if request.method == "POST":  # 登录方式
        usernm = request.POST.get("username")  # 获取用户名
        passwd = request.POST.get("password")  # 获取密码

        user = Userinfo.objects.filter(username=usernm)  # 到数据库查询
        if len(user) == 1:
            print(common.cmd5(str(passwd)) == user[0].password)
            if common.cmd5(str(passwd)) == user[0].password:
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


# 注册
def register(request):
    return render(request, 'register.html')


# 注册处理逻辑
def register_handler(request):
    resp = {'status': 400, 'msg': '非法注册'}
    if request.method == "POST":
        # 获取字段
        username = request.POST.get('zphone')
        msgcode = request.POST.get('zcode1')
        passwd1 = request.POST.get('zpass')
        passwd2 = request.POST.get('zpass2')
        if (passwd1 == passwd2):
            if (request.session.get('msgcode') == msgcode):  # 验证码
                user = Userinfo()
                user.username = username
                print(passwd1)
                user.password = common.cmd5(str(passwd1))
                print(user.password)
                user.save()
                resp['status'] = 200
                resp['msg'] = '注册成功，请登录'
                return render(request, 'login.html', resp)
            else:
                resp['msg'] = '验证码不正确'
                return render(request, 'register.html', resp)
        else:
            resp['msg'] = '两次密码不一致'
            return render(request, 'register.html', resp)

    return render(request, 'register.html', resp)


# 发送短信验证码
def register_sendmessage(request):
    # 获取电话号码
    moblie = request.GET.get('phone')
    # print(moblie)
    # 通过手机去查找用户是否已经注册
    user = Userinfo.objects.filter(username=moblie)
    if len(user) == 1:
        resp = {'status': 400, 'msg': '该手机已注册'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        # msgcode, response_str = common.send_message(moblie)
        # print(msgcode, response_str)
        msgcode, response_str = '123456', b'{"code":2,"msg":"\\u63d0\\u4ea4\\u6210\\u529f","smsid":"15464153595432868415"}'
        request.session['msgcode'] = msgcode
        resp = {'status': 200, 'msg': response_str.decode()}
        return HttpResponse(json.dumps(resp), content_type="application/json")


# 发送短信验证码
def upass_sendmessage(request):
    # 获取电话号码
    moblie = request.GET.get('phone')
    # print(moblie)
    # 通过手机去查找用户是否已经注册
    user = Userinfo.objects.filter(username=moblie)
    if len(user) == 1:
        # msgcode, response_str = common.send_message(moblie)
        # print(msgcode, response_str)
        msgcode, response_str = '123456', b'{"code":2,"msg":"\\u63d0\\u4ea4\\u6210\\u529f","smsid":"15464153595432868415"}'
        request.session['msgcode'] = msgcode
        resp = {'status': 200, 'msg': response_str.decode()}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'status': 400, 'msg': '帐号不存在'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


# 获取图像验证码
def getcodeimg(request):
    f = BytesIO()  # 返回字节流
    im, code = common.genCode(80, 40, 30)  # 获取验证码
    request.session['code'] = code.lower()  # 设置session验证码
    im.save(f, 'PNG')  # 将图像转为字节流

    return HttpResponse(f.getvalue(), "image/PNG")


# 获取验证码
def getcode(request):
    resp = {}
    resp['code'] = request.session.get('code')
    return HttpResponse(json.dumps(resp), content_type="application/json")


# 忘记密码
def upass(request):
    return render(request, 'upass.html')


# 忘记密码逻辑处理
def upass_handler(request):
    resp = {'status': 400, 'msg': '非法修改'}
    if request.method == "POST":
        # 获取字段
        username = request.POST.get('zphone')
        msgcode = request.POST.get('zcode1')
        passwd1 = request.POST.get('zpass')
        passwd2 = request.POST.get('zpass2')
        if (passwd1 == passwd2):
            if (request.session.get('msgcode') == msgcode):  # 验证码
                user = Userinfo.objects.filter(username=username)
                if len(user) == 1:
                    user = user[0]
                    user.password = common.cmd5(str(passwd1))
                    user.save()
                    resp['status'] = 200
                    resp['msg'] = '修改成功，请登录'
                    return render(request, 'login.html', resp)
                else:
                    resp['msg'] = '用户不存在'
                    return render(request, 'upass.html', resp)
            else:
                resp['msg'] = '验证码不正确'
                return render(request, 'upass.html', resp)
        else:
            resp['msg'] = '两次密码不一致'
            return render(request, 'upass.html', resp)

    return render(request, 'upass.html', resp)
