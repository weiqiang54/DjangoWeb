from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout

from utils.mixin_utils import LoginRequireMixin
from utils.alipay import AliPay
from .models import UserProfile
from alipay.settings import pub_key_path, private_key_path


class RegisterView(View):
    """
    注册
    """
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')

        if user and pwd:
            had_reg = UserProfile.objects.filter(username=user)
            if had_reg:
                return HttpResponse('用户名已被注册')
            else:
                new_user = UserProfile()
                new_user.username = user
                new_user.password = make_password(pwd)
                new_user.save()
                return redirect('/login/')
        else:
            return HttpResponse('未收到注册数据')


class LoginView(View):
    """
    登录
    """
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user_name = request.POST.get('username', '')
        password = request.POST.get('pwd', '')
        if user_name and password:
            user = authenticate(username=user_name, password=password)
            if user:
                login(request, user)
                return redirect('/shop/')
        return HttpResponse('有错误')


class ShopView(LoginRequireMixin, View):
    """
    购物
    """
    def get(self, request):
        return render(request, 'shop.html', {'user': request.user})

    def post(self, request):
        alipay = AliPay(
            appid='2016091500517256',
            app_notify_url='http://192.168.18.153:8000/shop/',
            app_private_key_path=private_key_path,
            alipay_public_key_path=pub_key_path,
            debug=True,
            return_url='http://192.168.18.153:8000/shop/',
        )
        url = alipay.direct_pay(
            subject='你的背包',
            out_trade_no='20200404aaa1',
            total_amount=100,
            return_url='http://192.168.18.153:8000/alipay/return/'
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        print(re_url)

        return redirect(re_url)


