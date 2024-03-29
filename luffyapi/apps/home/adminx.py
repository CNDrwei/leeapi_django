import xadmin

# 配置主题
from xadmin import views


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "路飞学城"  # 设置站点标题
    site_footer = "路飞学城有限公司"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠


xadmin.site.register(views.CommAdminView, GlobalSettings)

from . import models

xadmin.site.register(models.Banner)
xadmin.site.register(models.Navigation)
