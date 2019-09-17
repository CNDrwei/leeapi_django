from django.db import models
from utils.model import BaseModel


class Banner(BaseModel):
    name = models.CharField(verbose_name='标题', max_length=16)
    note = models.TextField(verbose_name='备注信息', max_length=150)
    image = models.ImageField(verbose_name='图片', upload_to='banner')
    link = models.CharField(verbose_name='链接', max_length=64)

    class Meta:
        db_table = 'luffy_banner'
        verbose_name = '轮播图表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Navigation(BaseModel):
    '''导航栏'''
    NAV_CHOICE = (
        (0, '顶部导航'),
        (1, '底部导航')
    )

    name = models.CharField(max_length=50, verbose_name='导航名称')
    link = models.CharField(max_length=350, verbose_name='导航地址')
    opt = models.SmallIntegerField(choices=NAV_CHOICE, default=0, verbose_name='位置')

    class Meta:
        db_table = 'luffy_navigation'
        verbose_name = '导航条'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
