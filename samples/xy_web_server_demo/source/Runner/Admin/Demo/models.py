import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class MDemo(models.Model):
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

    text = models.TextField(
        verbose_name=_("文本"),
        null=True,
        blank=True,
        default="",
    )

    image = models.ForeignKey(
        "Resource.MImage",
        verbose_name=_("图片"),
        related_name="%(app_label)s_%(class)s_images",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("样例")
        verbose_name_plural = _("样例")
        app_label = "Demo"

    def __str__(self):
        return f"{self.id}. {self.update_at} - {self.text}"
