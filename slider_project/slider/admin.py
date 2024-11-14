from django.contrib import admin
from .models import SliderItem
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail')
    search_fields = ('title',)

    # Создаем метод для отображения миниатюры изображения в админке
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" />', obj.image.url)
        return ""

    image_thumbnail.short_description = 'Миниатюра'

