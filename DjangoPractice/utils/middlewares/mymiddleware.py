from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, render, HttpResponse
from django.conf import settings
from app01.models import *

class CheckLogin(MiddlewareMixin):
    def process_request(self, request):
        while_urls  = settings.WHITE_URLS if hasattr(settings, 'WHITE_URLS') else []
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