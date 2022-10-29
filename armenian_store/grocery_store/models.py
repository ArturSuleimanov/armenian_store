from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    title = models.TextField(max_length=100, verbose_name='Наименование')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default="photos/default.png", verbose_name='Фото')
    description = models.TextField(max_length=1024, default=None, blank=True, null=True,verbose_name='Описание')
    composition = models.TextField(max_length=1024, default=None, blank=True, null=True, verbose_name='Состав')
    nutritional_value = models.TextField(max_length=512, default=None, blank=True, null=True, verbose_name='Пищевая ценность')
    weight = models.PositiveIntegerField(blank=True, null=True, verbose_name='Масса')
    price = models.PositiveIntegerField(verbose_name='Цена')
    price_with_discount = models.PositiveIntegerField(verbose_name='Цена со скидкой',  default=None, blank=True, null=True,)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_page', kwargs={'product_id': self.pk})


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Категория")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']

    def __str__(self):
        return self.title