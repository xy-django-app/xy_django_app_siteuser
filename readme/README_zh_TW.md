<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:56
 * @FilePath: /xy_django_app_siteuser/readme/README_zh_TW.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_siteuser

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## 說明

通用資訊資料模型.

## 程式碼庫

- <a href="https://github.com/xy-django-app/xy_django_app_siteuser.git" target="_blank">Github位址</a>  
- <a href="https://gitee.com/xy-django-app/xy_django_app_siteuser.git" target="_blank">Gitee位址</a>

## 安裝

```bash
# bash
pip install xy_django_app_siteuser
```

## 使用


#### 1. 建立SiteUser模組
> 操作 [样例工程](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp SiteUser
# SiteUser 模块创建在 source/Runner/Admin/SiteUser 
```

#### 2. 在範例工程中的[settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)设置如下

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Demo",
    "Resource",
    "Media",
    "Information",
    "SiteUser",
]

```

#### 3. 在[SiteUser](../samples/xy_web_server_demo/source/Runner/Admin/SiteUser)模組的[models.py](../samples/xy_web_server_demo/source/Runner/Admin/SiteUser/models.py)檔中加入如下程式碼

```python
# models.py
from django.db import models

from django.utils.translation import gettext_lazy as _
from xy_django_app_siteuser.abstracts import (
    MAAuthUser,
    MAAuthUserCredential,
    MACaptcha,
    MAEmailCredential,
    MASiteUser,
    MASMSCaptchaCredential,
)


class MEmailCredential(MAEmailCredential):
    class Meta:
        app_label = "SiteUser"
        verbose_name = _("邮箱凭证")
        verbose_name_plural = _("邮箱凭证")


class MCaptcha(MACaptcha):
    class Meta:
        app_label = "SiteUser"
        verbose_name = _("验证码")
        verbose_name_plural = _("验证码")


class MSMSCaptchaCredential(MASMSCaptchaCredential):
    class Meta:
        app_label = "SiteUser"
        verbose_name = _("短信凭证")
        verbose_name_plural = _("短信凭证")


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
        app_label = "SiteUser"
        verbose_name = _("邮箱验证码")
        verbose_name_plural = _("邮箱验证码")

    def __str__(self):
        return str(self.id) + ". " + str(self.code)


class MSMSCaptcha(MACaptcha):
    mobile = models.CharField(
        verbose_name=_("手机号"),
        max_length=255,
    )

    class Meta:
        app_label = "SiteUser"
        verbose_name = _("短信验证码")
        verbose_name_plural = _("短信验证码")

    def __str__(self):
        return str(self.id) + ". " + str(self.code)


class MSiteUser(MASiteUser):
    region = models.ForeignKey(
        "Information.MRegion",
        verbose_name=_("所在地"),
        related_name="%(app_label)s_%(class)s_region",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        app_label = "SiteUser"
        verbose_name = _("站点用户")
        verbose_name_plural = _("站点用户")


class MAuthUserCredential(MAAuthUserCredential):
    class Meta:
        app_label = "SiteUser"
        verbose_name = _("授权用户凭证")
        verbose_name_plural = _("授权用户凭证")


class MAuthUser(MAAuthUser):
    credential = models.ForeignKey(
        "SiteUser.MAuthUserCredential",
        verbose_name=_("授权用户凭证"),
        related_name="%(app_label)s_%(class)s_credential",
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        app_label = "SiteUser"
        verbose_name = _("授权用户凭证")
        verbose_name_plural = _("授权用户凭证")


```

#### 4. 在[SiteUser](../samples/xy_web_server_demo/source/Runner/Admin/SiteUser)模組的[admin.py](../samples/xy_web_server_demo/source/Runner/Admin/SiteUser/admin.py)檔中加入如下程式碼

```python
# admin.py
from django.contrib import admin
from .models import (
    MAuthUser,
    MAuthUserCredential,
    MCaptcha,
    MEmailCaptcha,
    MEmailCredential,
    MSiteUser,
    MSMSCaptcha,
    MSMSCaptchaCredential,
)


@admin.register(MEmailCredential)
class AEmailCredential(admin.ModelAdmin):
    pass


@admin.register(MCaptcha)
class ACaptcha(admin.ModelAdmin):
    pass


@admin.register(MSMSCaptchaCredential)
class ASMSCaptchaCredential(admin.ModelAdmin):
    pass


@admin.register(MEmailCaptcha)
class AEmailCaptcha(admin.ModelAdmin):
    pass


@admin.register(MSMSCaptcha)
class ASMSCaptcha(admin.ModelAdmin):
    pass


@admin.register(MSiteUser)
class ASiteUser(admin.ModelAdmin):
    search_fields = ["id", "name", "email", "username", "identifier"]
    autocomplete_fields = ["region"]


@admin.register(MAuthUserCredential)
class AAuthUserCredential(admin.ModelAdmin):
    pass


@admin.register(MAuthUser)
class AuthUser(admin.ModelAdmin):
    pass

```

#### 5. 运行项目

```bash
xy_web_server -w django start
# 啟動工程後請造訪 http://127.0.0.1:8401/admin 驗證網站使用者管理系統
```

##### 運轉 [範例工程](../samples/xy_web_server_demo)

> 範例工程具體使用方式請移步 <b style="color: blue">xy_web_server.git</b> 下列倉庫
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github位址</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee位址</a>

## 許可證
xy_django_app_siteuser 根據 <木蘭寬鬆許可證, 第2版> 獲得許可。有關詳細信息，請參閱 [LICENSE](../LICENSE) 文件。

## 捐贈

如果小夥伴們覺得這些工具還不錯的話，能否請咱喝一杯咖啡呢?  

![Pay-Total](./Pay-Total.png)

## 聯繫方式

```
微信: yuyangiit
郵箱: yuyangit.0515@qq.com
```