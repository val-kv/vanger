from django.contrib import admin
from .models import SliderItem
from adminsortable2.admin import SortableAdminMixin


class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail')
    search_fields = ('title',)

    def image_thumbnail(self, obj):
        if obj.image:
            return obj.image.admin_thumbnail()
        return ""

    image_thumbnail.short_description = 'Preview'


admin.site.register(SliderItem, SliderItemAdmin)
