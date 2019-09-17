from rest_framework.serializers import ModelSerializer

from . import models


class BannerModelSerializer(ModelSerializer):
    class Meta:
        model = models.Banner
        fields = ('image', 'link')


class NavModelSerializer(ModelSerializer):
    class Meta:
        model = models.Navigation
        fields = ('name', 'link')
