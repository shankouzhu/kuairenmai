"""kuairenmai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from kuairenmai import settings
from django.conf.urls.static import static
from kuairenmai.autorouter import router

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'favicon.ico', RedirectView.as_view(url=r'/static/favicon.ico'), name='favicon'),
    re_path(r'^(?P<app>(\w+))/$', router, {'function': 'index'}),
    re_path(r'^(?P<app>(\w+))/(?P<function>(\w+))/$', router),
    re_path(r'^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\d+))$', router),
    re_path('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<page>(\d+))/(?P<id>(\d+))/$', router),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
