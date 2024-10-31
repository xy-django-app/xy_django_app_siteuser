from django.contrib import admin
from .models import MRegion

# Register your models here.


@admin.register(MRegion)
class ARegion(admin.ModelAdmin):
    search_fields = [
        "id",
        "name",
        "country",
        "province",
        "city",
        "district",
        "town",
        "address",
    ]
