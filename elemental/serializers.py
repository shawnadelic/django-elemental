from rest_framework import serializers

from .models import Menu


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ("title", "identifier")
