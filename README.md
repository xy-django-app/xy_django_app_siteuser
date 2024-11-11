<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:23
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:51:38
 * @FilePath: /xy_django_app_siteuser/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_siteuser

| [简体中文](./README.md)         | [繁體中文](readme/README.zh-hant.md)        |                      [English](readme/README.en.md)          |
| ----------- | -------------|---------------------------------------|

## 说明

通用站点用户数据模型.

## 源码仓库

| [Github](https://github.com/xy-django-app/xy_django_app_siteuser.git)         | [Gitee](https://gitee.com/xy-opensource/xy_django_app_siteuser.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_django_app_siteuser.git)          |
| ----------- | -------------|---------------------------------------|


## 安装

```bash
# bash
pip install xy_django_app_siteuser
```

## 使用


##### 1. 直接引入

- ###### 1. 设置全局配置

在Django项目中的settings.py文件中加入如下配置
例如: [settings.py](./samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_siteuser",
    "Demo",
    "Media",
]
```

- ###### 2. 运行项目

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证站点管理系统
```

##### 2. 自定义

- ###### 1. 创建SiteUser模块

> 操作 [样例工程](./samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp SiteUser
# SiteUser 模块创建在 source/Runner/Admin/SiteUser 
```

- ###### 2. 设置全局配置

在Django项目中的settings.py文件中加入如下配置
例如: [settings.py](./samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

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
    "Media",
    "SiteUser",
]

```

- ###### 3. 在[SiteUser](./samples/xy_web_server_demo/source/Runner/Admin/SiteUser)模块的[models.py](./samples/xy_web_server_demo/source/Runner/Admin/SiteUser/models.py)文件中加入如下代码

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

- ###### 4. 在[SiteUser](./samples/xy_web_server_demo/source/Runner/Admin/SiteUser)模块的[admin.py](./samples/xy_web_server_demo/source/Runner/Admin/SiteUser/admin.py)文件中加入如下代码

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

- ###### 5. 运行项目

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证站点用户管理系统
```


##### 运行 [样例工程](./samples/xy_web_server_demo)

> 样例工程具体使用方式请移步 <b style="color: blue">xy_web_server.git</b> 下列仓库

| [Github](https://github.com/xy-web-service/xy_web_server.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_server.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_server.git)          |
| ----------- | -------------|---------------------------------------|


## 许可证
xy_django_app_siteuser 根据 <木兰宽松许可证, 第2版> 获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 捐赠
如果小伙伴们觉得这些工具还不错的话，能否请咱喝一杯咖啡呢?  

![Pay-Total](./readme/Pay-Total.png)


## 联系方式

```
微信: yuyangiit
邮箱: yuyangit.0515@qq.com
```