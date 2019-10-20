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

#才用第二种class-based views

from django.contrib import admin
from django.urls import include, path

from InstaApp.views import HelloDjango, PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', HelloDjango.as_view(), name = 'helloDjango'),
    #当传入是空字符串的时候，去调用 HelloDjango 里面的 as_view 的函数
    #由于 HelloDjango 继承了 TemplateView，所以相应的 as_view 方法也会被继承下来

    path('posts/', PostView.as_view(), name = 'posts'),
    #测试时使用这个语句http://localhost:8000/instaapp/posts/
    #因为posts是在instaapp的下一个分支

    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    #<int:pk>代表这里用户会提供一个integer，然后这个integer Django要将它以primary key来看待
    #假如是1，收到这个要求后会在Post这个列表中找看哪个id等于1，找到之后会把它rander在post_detail的html上面

    path('post/new/', PostCreateView.as_view(), name = 'make_post'),

    path('post/update/<int:pk>/', PostUpdateView.as_view(), name = 'post_update'),

    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name = 'post_delete'),
]
