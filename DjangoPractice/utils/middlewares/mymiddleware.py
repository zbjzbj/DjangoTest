from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render, HttpResponse
from django.conf import settings
from app01.models import *
import time


# 登陆验证中间件
class CheckLogin(MiddlewareMixin):
    def process_request(self, request):
        while_urls = settings.WHITE_URLS if hasattr(settings, 'WHITE_URLS') else []
        if request.path_info in while_urls:
            return None

        is_login = request.session.get('user')
        if not is_login:
            # 没有登录，跳转到登录界面
            # 获取当前访问的url
            next_url = request.path_info
            return redirect('/login/?returnUrl={}'.format(next_url))
        # 已经登录了,获取登录的对象
        user_obj = Userinfo.objects.get(name=is_login)
        # 把登录对象赋值给request的use属性(自定义属性)
        request.user = user_obj


# 频率限制中间件
# 存放每个ip访问页面的大字典
ACCESS_RECORD = dict()


class Throttle(MiddlewareMixin):
    def process_request(self, request):
        access_limit = settings.ACCESS_LIMIT if hasattr(settings, 'ACCESS_LIMIT') else 10
        ip = request.META.get('REMOVE_ADDR')
        if ip not in ACCESS_RECORD:
            ACCESS_RECORD[ip] = list()
        ip_access_list = ACCESS_RECORD[ip]

        now = time.time()
        while ip_access_list and now - ip_access_list[-1] > access_limit:
            ip_access_list.pop()

        ip_access_list.insert(0, now)
        if len(ip_access_list) > 3:
            return HttpResponse('滚')
