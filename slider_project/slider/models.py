from django.db import models
from filer.fields.image import FilerImageField


class SliderItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = FilerImageField(related_name="slider_images", on_delete=models.CASCADE, verbose_name="Изображение")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        ordering = ['id']
        verbose_name = "Элемент слайдера"
        verbose_name_plural = "Элементы слайдера"

    def __str__(self):
        return self.title
rrer