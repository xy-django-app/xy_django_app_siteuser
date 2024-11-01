<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_django_app_siteuser/readme/README_en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_siteuser

- [简体中文](README_zh_CN.md)
- [繁体中文](README_zh_TW.md)
- [English](README_en.md)

## Description

Common SiteUser data model.

## Source Code Repositories

- <a href="https://github.com/xy-django-app/xy_django_app_siteuser.git" target="_blank">Github</a>  
- <a href="https://gitee.com/xy-django-app/xy_django_app_siteuser.git" target="_blank">Gitee</a>

## Installation

```bash
# bash
pip install xy_django_app_siteuser
```

## How to use

##### 1. Direct import

- ###### 1. Setting global configuration

Add the following configuration to the settings.py file in the Django project  
For example: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

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

- ###### 2. Run the project

```bash
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证站点管理系统
```

##### 2. Custom

- ###### 1. Create SiteUser Module

> Operation [Sample Project](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp SiteUser
# SiteUser 模块创建在 source/Runner/Admin/SiteUser 
```

- ###### 2. Setting global configuration

Add the following configuration to the settings.py file in the Django project  
For example: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

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

- ###### 3. Add the following code to the [models.py](../samples/xy_web_server_demo/source/Runner/Admin/SiteUser/models.py) file of the  [SiteUser](../samples/xy_web_server_demo/source/Runner/Admin/SiteUser) module

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

- ###### 4. 在[SiteUser](../samples/xy_web_server_demo/source/Runner/Admin/SiteUser)模块的[admin.py](../samples/xy_web_server_demo/source/Runner/Admin/SiteUser/admin.py)文件中加入如下代码

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

- ###### 5. Run the project

```bash
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证站点用户管理系统
```

##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b> 
> - <a href="https://github.com/xy-web-service/xy_web_server.git" target="_blank">Github</a>  
> - <a href="https://gitee.com/xy-web-service/xy_web_server.git" target="_blank">Gitee</a>

## License
xy_django_app_siteuser is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![Pay-Total](./Pay-Total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```