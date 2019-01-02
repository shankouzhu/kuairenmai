from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import Userinfo
import json

# Create your views here.
def unpass(request):
    return render(request,'upass.html')
