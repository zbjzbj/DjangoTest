from django.shortcuts import render, HttpResponse, redirect
from functools import wraps
from django import views
from app01.models import *
from django.http import JsonResponse
from app01.my_forms import *


# Create your views here.

def tem(request):
    return render(request, "son-tmp.html", {"name": "小明"})

# 正常注册
# def register(request):
#     form_obj = HookForm()
#     if request.method == "POST":
#         form_obj = HookForm(request.POST)
#         if form_obj.is_valid():
#             # 数据库中创建
#             return redirect('/index/')
#         return render(request, 'register.html', {"form_obj": form_obj})
#     return render(request, 'register.html', {"form_obj": form_obj})


# ajax注册
def register(request):
    if request.method == 'POST':
        res = {'code': 0}
        # 利用post提交的数据实例化form类
        form_obj = RegModelForm(request.POST)
        # 校验数据的有效性
        if form_obj.is_valid():
            form_obj.cleaned_data.pop('re_pwd')
            # Userinfo.objects.create(**form_obj.cleaned_data)
            # form_obj.save()
            res['url'] = '/login/'
        else:
            # 数据有问题
            res['code'] = 1
            res['error_msg'] = form_obj.errors
        return JsonResponse(res)

    form_obj = RegModelForm()
    return render(request, 'register.html', {'form_obj': form_obj})

############## COOKIE 版登陆 ##############
# def check_login(func):
#     @wraps(func)
#     def inner(request, *args, **kwargs):
#         if request.COOKIES.get('xm') == 'sb':
#             rep = func(request, *args, **kwargs)
#             return rep
#         return_url = request.path_info
#         return redirect('/login?return_url={}'.format(return_url))
#
#     return inner
#
#
# class LoginView(views.View):
#
#     def get(self, request):
#         return render(request, "login.html")
#
#     def post(self, request):
#         username = request.POST.get('username')
#         pwd = request.POST.get('password')
#         is_rem = request.POST.get('remember', None)
#         is_ok = Userinfo.objects.get(name=username, password=pwd)
#         if is_ok:
#             # 判断是否从其他页面跳转到登录页面，拿到return_url
#             # 如果取不到returnUrl，默认跳转到index页面
#             return_url = request.GET.get('returnUrl', '/index/')
#             rep = redirect(return_url)  # rep就是响应对象
#             # 判断是否记住密码
#             if is_rem:
#                 # 是就保存七天
#                 rep.set_cookie('xm', 'sb', max_age=60 * 60 * 24 * 7)
#             else:
#                 # 不是就不保存
#                 rep.set_cookie('xm', 'sb')  # 告诉浏览器在自己本地保存一个键值对
#             return rep
#         else:
#             return render(request, 'login.html', {'error_msg': '用户名或者密码错误'})
#
# # 首页
# @check_login
# def index(request):
#     return render(request, 'tmp.html')


############# session版登陆 ##########

# 用装饰器做session登录验证
def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        # session版
        # 验证
        session_user = request.session.get('user', None)
        if session_user:
            rep = func(request, *args, **kwargs)
            return rep
        else:
            # 否则，让用户去登录
            # 拿到当前访问的url
            return_url = request.path_info
            return redirect('/login/?returnUrl={}'.format(return_url))
    return inner


# 登录
class LoginView(views.View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        # session版
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        is_rem = request.POST.get('remember', None)
        # 不推荐使用get,因为get取不到值会报错
        user_obj = Userinfo.objects.filter(name=username, password=pwd).first()
        if user_obj:
            return_url = request.GET.get('returnUrl', '/index/')
            request.session['user'] = user_obj.name
            # 判断是否记住密码
            if is_rem:
                # 是就保存七天
                request.session.set_expiry(60*60*24*7)
            else:
                # 不是的话关闭浏览器就失效
                request.session.set_expiry(0)
            return redirect(return_url)
        else:
            return render(request, 'login.html', {'error_msg': '用户名或者密码错误'})


# 首页
@check_login
def index(request):
    return render(request, 'tmp.html')


# 注销
def logout(request):
    # request.session.delete()  # 删除session
    request.session.flush()  # 删除session并让cookie失效
    return redirect('/login/')