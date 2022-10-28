from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_create', 'price', 'in_stock', 'price_with_discount']
    list_display_links = ['title', ]
    search_fields = ['title', 'description']
    list_editable = ['in_stock', 'price', 'price_with_discount']
    list_filter = ['in_stock', 'time_create']
    actions = ['title']

admin.site.register(Product, ProductAdmin)
admin.site.site_header = 'Администрирование'
