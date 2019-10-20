from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from InstaApp.models import Post
# 因为要views要控制model和template所以views中应该要包含model也要包含template
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from InstaApp.forms import CustomUserCreationForm

# Create your views here.
class HelloDjango(TemplateView):
    template_name = 'test.html'
# static的一个页面

class PostView(ListView):
    model = Post
    template_name = 'index.html'
# PostView继承ListView
# override （1）使用Post这个model（2）用template来显示

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    #在create的时候需要用户提供这个post的什么信息，这里选择需要提供所有的fields，但都不包括id
    login_url = 'login'
    #这里加入了LoginRequireMixin，意思是当create一个post的时候必须处于login的状态，如果不是的话跳转到login_url

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
    # 不能直接用reverse，用reverse相当于在删除的时候同时在跳转，reverse_lazy是删除后再跳转
    # 所以当用到类似delete的操作时候都用reverse_lazy

class SignUp(CreateView):
    #form_class = UserCreationForm
    form_class = CustomUserCreationForm
    # 这里替换成用户自定义的creation form, 使sign up的时候收集更多的用户信息
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

