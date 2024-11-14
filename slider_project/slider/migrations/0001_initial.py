# Generated by Django 4.2.16 on 2024-11-14 20:35

import adminsortable2.admin
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_images', to=settings.FILER_IMAGE_MODEL, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Элемент слайдера',
                'verbose_name_plural': 'Элементы слайдера',
                'ordering': ['id'],
            },
            bases=(adminsortable2.admin.SortableAdminMixin, models.Model),
        ),
    ]
