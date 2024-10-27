# -*- coding: UTF-8 -*-
__author__ = "helios"

from django.db import models
from django.utils.translation import gettext_lazy as _
from .abstracts import (
    MAAuthUser,
    MAAuthUserCredential,
    MACaptcha,
    MAEmailCredential,
    MASiteUser,
    MASMSCaptchaCredential,
)


class MEmailCredential(MAEmailCredential):
    class Meta:
        app_label = "xy_django_app_siteuser"


class MCaptcha(MACaptcha):
    class Meta:
        app_label = "xy_django_app_siteuser"


class MSMSCaptchaCredential(MASMSCaptchaCredential):
    class Meta:
        app_label = "xy_django_app_siteuser"


class MEmailCaptcha(MACaptcha):
    from_email = models.CharField(
        verbose_name=_("发送方邮箱"),
        max_length=255,
    )
    to_email = models.CharField(
        verbose_name=_("目标邮箱"),
        max_length=255,
    )

    class Meta:
        app_label = "xy_django_app_siteuser"

    def __str__(self):
        return str(self.id) + ". " + str(self.code)


class MSMSCaptcha(MACaptcha):
    mobile = models.CharField(
        verbose_name=_("手机号"),
        max_length=255,
    )

    class Meta:
        app_label = "xy_django_app_siteuser"

    def __str__(self):
        return str(self.id) + ". " + str(self.code)


class MSiteUser(MASiteUser):
    region = models.ForeignKey(
        "xy_django_app_information.MRegion",
        verbose_name=_("所在地"),
        related_name="%(app_label)s_%(class)s_region",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = "xy_django_app_siteuser"


class MAuthUserCredential(MAAuthUserCredential):
    class Meta:
        app_label = "xy_django_app_siteuser"


class MAuthUser(MAAuthUser):
    credential = models.ForeignKey(
        "xy_django_app_siteuser.MAuthUserCredential",
        verbose_name=_("授权用户凭证"),
        related_name="%(app_label)s_%(class)s_credential",
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        app_label = "xy_django_app_siteuser"
