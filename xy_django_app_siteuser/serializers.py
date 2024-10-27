# -*- coding: UTF-8 -*-
__author__ = "helios"
__doc__ = "serializers"
"""
  * @File    :   serializers.py
  * @Time    :   2023/05/04 14:33:41
  * @Author  :   余洋
  * @Version :   1.0
  * @Contact :   yuyang.0515@qq.com
  * @License :   (C)Copyright 2019-2023, 希洋 (Ship of Ocean)
  * @Desc    :   None
"""

from .models import (
    MSiteUser,
    MSMSCaptcha,
    MSMSCaptchaCredential,
    MAuthUser,
    MAuthUserCredential,
    MEmailCaptcha,
    MEmailCredential,
    MCaptcha,
)
from rest_framework import viewsets, serializers
from xy_admin_model_serializer.Admin_ModelSerializer import (
    Admin_ModelSerializer,
)


class SSiteUser(Admin_ModelSerializer):
    default_value = ""
    thumb_url = serializers.ReadOnlyField()

    class Meta:
        model = MSiteUser
        fields = "__all__"


class VSSiteUser(viewsets.ModelViewSet):
    queryset = MSiteUser.objects.all()
    serializer_class = SSiteUser


class SEmailCredential(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MEmailCredential
        fields = "__all__"


class VSEmailCredential(viewsets.ModelViewSet):
    queryset = MEmailCredential.objects.all()
    serializer_class = SEmailCredential


class SCaptcha(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MCaptcha
        fields = "__all__"


class VSCaptcha(viewsets.ModelViewSet):
    queryset = MCaptcha.objects.all()
    serializer_class = SCaptcha


class SSMSCaptchaCredential(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MSMSCaptchaCredential
        fields = "__all__"


class VSSMSCaptchaCredential(viewsets.ModelViewSet):
    queryset = MSMSCaptchaCredential.objects.all()
    serializer_class = SSMSCaptchaCredential


class SEmailCaptcha(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MEmailCaptcha
        fields = "__all__"


class VSEmailCaptcha(viewsets.ModelViewSet):
    queryset = MEmailCaptcha.objects.all()
    serializer_class = SEmailCaptcha


class SSMSCaptcha(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MSMSCaptcha
        fields = "__all__"


class VSSMSCaptcha(viewsets.ModelViewSet):
    queryset = MSMSCaptcha.objects.all()
    serializer_class = SSMSCaptcha


class SAuthUserCredential(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MAuthUserCredential
        fields = "__all__"


class VSAuthUserCredential(viewsets.ModelViewSet):
    queryset = MAuthUserCredential.objects.all()
    serializer_class = SAuthUserCredential


class SAuthUser(Admin_ModelSerializer):
    default_value = ""

    class Meta:
        model = MAuthUser
        fields = "__all__"


class VSAuthUser(viewsets.ModelViewSet):
    queryset = MAuthUser.objects.all()
    serializer_class = SAuthUser
