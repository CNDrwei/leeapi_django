from rest_framework.generics import ListAPIView
from . import models, serializers
from utils.APIResponse import APIResponse
from django.core.cache import cache

# 自动刷新轮播图
class BannerListAPIView(ListAPIView):
    queryset = models.Banner.objects.filter(is_show=True, is_delete=False).order_by('orders')
    serializer_class = serializers.BannerModelSerializer

    def get(self, request, *args, **kwargs):
        banner_obj_list = cache.get('api_banner_list_data')
        if not banner_obj_list:
            print('查询了数据库')
            banner_query = models.Banner.objects.filter(
                is_delete=False, is_show=True).order_by('orders')
            banner_obj_list = serializers.BannerModelSerializer(banner_query, many=True).data

            # print(banner_obj_list, type(banner_obj_list))
            cache.set('banner_obj_list', banner_obj_list)

        return APIResponse(0, 'ok', results=banner_obj_list)

# 手动刷新轮播图












