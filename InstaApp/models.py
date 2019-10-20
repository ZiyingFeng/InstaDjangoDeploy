from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField

from django.contrib.auth.models import AbstractUser

# Create your models here.
# 创建一个名为Post的类，并且这个类继承models.Model
class Post(models.Model):
    title = models.TextField(blank = True, null = True)
    # 定义了一个title，这个title是一个TextField，括号中意思是说空的或者null的都可以发出去
    image = ProcessedImageField(
        upload_to = 'statics/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
    )
    # 由于models自带的ImageField不够强大，所以使用安装一个imagekit，使用它的ProcessedImageField

    def get_absolute_url(self):
        # self指当前object，因为Post是一个类，并不是一个object
        # return reverse("helloDjango")
        # reverse从urls.py寻找名字为helloDjango的url
        return reverse("post_detail", args=[str(self.id)])


class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'statics/images/posts',
        format = 'JPEG',
        options = {'quality':100},
        blank = True,
        null = True
    )
# 这是一个用户自定义的替代auth自带的model，因为有时候注册的时候需要知道profile picture或收集更多其他信息而不只是名字密码


class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        # 当post被删除的时候所有的Like都被删除，这是on_delete = models.CASCADE这句的意思
        related_name = "likes"
    )
