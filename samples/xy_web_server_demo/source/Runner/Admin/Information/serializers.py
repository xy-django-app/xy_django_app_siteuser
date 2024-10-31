# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "serializers"
"""
  * @File    :   serializers.py
  * @Time    :   2023/05/01 21:25:03
  * @Author  :   helios
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, Ship of Ocean
  * @Desc    :   None
"""

from xy_django_serializer.Serializer import Serializer
from .models import MRegion


class SRegion(Serializer):
    default_value = ""

    class Meta:
        model = MRegion
        fields = "__all__"
