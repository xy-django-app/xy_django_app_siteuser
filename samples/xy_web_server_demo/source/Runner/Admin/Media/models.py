import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models

from xy_django_model.model import gen_upload_to


# Create your models here.
def movies(instance=None, filename=None):
    return "/".join(["Media_MMovie", instance.identifier.hex, filename])


class MMovie(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_at = models.DateTimeField(
        verbose_name=_("创建时间"),
        auto_now_add=True,
        editable=True,
    )
    update_at = models.DateTimeField(
        verbose_name=_("更新时间"),
        auto_now_add=True,
        editable=True,
    )
    identifier = models.UUIDField(
        verbose_name=_("唯一标识"),
        default=uuid.uuid4,
        editable=True,
        unique=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name=_("是否启用"),
        null=True,
        blank=True,
        default=False,
    )
    movie = models.FileField(
        verbose_name=_("电影文件"),
        upload_to=movies,
        null=True,
        blank=True,
        default=None,
        help_text=_("图片"),
    )

    class Meta:
        verbose_name = _("电影")
        verbose_name_plural = _("电影")
        app_label = "Media"

    def __str__(self):
        return f"{self.id}. {self.identifier}"
