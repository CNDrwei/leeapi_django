from django.db import models
class BaseModel(models.Model):
    orders = models.IntegerField(verbose_name='显示顺序')
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True, null=True, blank=True)
    updated_time = models.DateTimeField(verbose_name="更新时间", auto_now=True, null=True, blank=True)
    is_show = models.BooleanField(verbose_name="是否上架", default=False)
    is_delete = models.BooleanField(verbose_name="逻辑删除", default=False)
    class Meta:
        abstract = True

