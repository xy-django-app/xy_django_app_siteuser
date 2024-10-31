from django.contrib import admin

# Register your models here.
from .models import MImage


@admin.register(MImage)
class AImage(admin.ModelAdmin):
    list_per_page = 20
    filter_horizontal = []
    list_display_links = [
        "id",
        "identifier",
        "update_at",
        "create_at",
    ]
    list_display = [
        "id",
        "identifier",
        "update_at",
        "create_at",
    ]
    search_fields = list_display
    autocomplete_fields = [
        # "id",
        # "communicate_at",
        # "identifier",
    ]
