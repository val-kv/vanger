from django.contrib import admin
from .models import SliderItem
from adminsortable2.admin import SortableAdminMixin
from easy_thumbnails.files import get_thumbnailer


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'admin_thumbnail_preview')
    search_fields = ('title',)
    readonly_fields = ('admin_thumbnail_preview',)

    # Создаем метод для отображения миниатюры изображения в админке
    def admin_thumbnail_preview(self, obj):
        if obj.image:
            thumbnail_url = get_thumbnailer(obj.image)['admin_thumbnail'].url
            return f'<img src="{thumbnail_url}" alt="{obj.title}" style="border-radius: 8px;"/>'
        return "Нет изображения"

    admin_thumbnail_preview.short_description = "Превью"
    admin_thumbnail_preview.allow_tags = True

