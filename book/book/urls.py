"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

# from users import views
# from demo2.views import TypeView
# from demo4.views import SendCodeView, RegisterVIew, SendActiveCodeView, ActivaView
from demo5.views import IndexView

# router = DefaultRouter()
# router.register(r'apibook5', views.BookModelViewSet)


# Django REST framework的三层封装
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/book1/', views.BookAPIView1.as_view(), name='book1'),
    # path('api/book2/', views.BookAPIView2.as_view(), name='book2'),
    # path('api/book3/', views.BookMixinView1.as_view(), name='book3'),
    # path('api/book4/', views.BookMixinView2.as_view(), name='book4'),
    # path('', include(router.urls)),
]

# 大型电商类别表
urlpatterns += [
    # path('api/types/', TypeView.as_view(), name='types'),
]

# 认证业务模型
# urlpatterns += [
#     path('sendcode/', SendCodeView.as_view(), name='sendcode'),
#     path('register/', RegisterVIew.as_view(), name='register'),
#     path('sendactivecode/', SendActiveCodeView.as_view(), name='sendactivecode'),
#     path('active/', ActivaView.as_view(), name='active'),
# ]

# JWT认证
urlpatterns += [
    path('jwt-token-auth/', obtain_jwt_token),
    path('index/', IndexView.as_view(), name='index'),
]

