from rest_framework.generics import ListAPIView
from . import models, serializers
class BannerListAPIView(ListAPIView):
    queryset = models.Banner.objects.filter(is_show=True, is_delete=False).order_by('-orders')
    serializer_class = serializers.BannerModelSerializer

