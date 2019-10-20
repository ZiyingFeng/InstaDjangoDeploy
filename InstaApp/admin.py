from django.contrib import admin

from InstaApp.models import Post, InstaUser

# Register your models here.
admin.site.register(Post)
#在admin这个app里面注册Post这个model，这样就能在admin后台中监测各种类的数据
admin.site.register(InstaUser)
