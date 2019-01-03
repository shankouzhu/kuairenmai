from django.shortcuts import render

# Create your views here.
#需求发布页面
def demandnew(request):
    return render(request,'demand/demandnew.html')
