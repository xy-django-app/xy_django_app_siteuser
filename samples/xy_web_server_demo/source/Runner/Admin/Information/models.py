# Create your models here.
from xy_django_app_information.abstracts import MARegion

from django.utils.translation import gettext_lazy as _


class MRegion(MARegion):
    class Meta:
        app_label = "Information"
        verbose_name = _("地理信息")
        verbose_name_plural = _("地理信息")
