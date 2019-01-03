from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Userinfo
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
import json
# Create your views here.
def unpass(request):
    return render(request,'upass.html')
def virifycode(request):
    width = 80
    height = 40
    bgcolor = 'green'
    im = Image.new('RGB',(width,height),bgcolor)
    # draw = ImageDraw(im)
    ios = BytesIO()
    im.save(ios,'png')
    return HttpResponse(ios.getvalue(),'image/png')


