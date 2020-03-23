from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
    用户信息
    """
    APIkey = models.CharField(max_length=30, verbose_name='APIkey', default='abcdefghigklmn')
    money = models.IntegerField(default=10, verbose_name='余额')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Book(models.Model):
    """
    书籍信息
    """
    title = models.CharField(max_length=30, verbose_name='书名', default='')
    isbn = models.CharField(max_length=30, verbose_name='书号', default='')
    author = models.CharField(max_length=20, verbose_name='作者', default='')
    publish = models.CharField(max_length=20, verbose_name='', default='')


