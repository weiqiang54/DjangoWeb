from django.db import models


class Types(models.Model):
    """类别表"""
    CATEGORY_TYPE = (
        (1, '一级类别'),
        (2, '二级类别'),
        (3, '三级类别'),
        (4, '四级类别'),
    )

    name = models.CharField(default='', max_length=30, verbose_name='类别名')
    code = models.CharField(default='', max_length=100, verbose_name='类别code')
    desc = models.CharField(default='', max_length=100, verbose_name='类别描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='所属分类')
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='父级类别')
    is_tab = models.BooleanField(default=False, verbose_name='是否导航')

    class Meta:
        verbose_name = '类别表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



