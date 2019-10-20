"""Insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from InstaApp.views import SignUp
#这里使用了第三种including another URLconf
urlpatterns = [
    path('admin/', admin.site.urls),
    path('instaapp/', include('InstaApp.urls')),
    #因为本来就是一个python文件所以include中不用写.py
    #这句的意思是当有人传送insta/的时候，请寻找InstaApp下面的urls.py这个文件
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup', SignUp.as_view(), name='signup'),
]
