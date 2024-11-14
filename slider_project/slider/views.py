from django.shortcuts import render
from .models import SliderItem


def slider_view(request):
    slider_items = SliderItem.objects.all()
    return render(request, 'slider/index.html', {'slider_items': slider_items})
