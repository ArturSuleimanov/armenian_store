from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_show', 'title', 'in_stock', 'price', 'price_with_discount',  'time_create']
    list_display_links = ['title', ]
    search_fields = ['title', 'description']
    list_editable = ['in_stock', 'price', 'price_with_discount']
    list_filter = ['in_stock', 'category', 'time_create']
    actions = ['title']

    def image_show(self, obj):
        if obj.photo:
            return mark_safe("<img src='{}' width='60'/>".format(obj.photo.url))
        return None

    image_show.__name__ = "Фото"

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.site_header = 'Администрирование'
