from django import forms
from django.forms import ModelForm
from grocery_store.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'composition', 'nutritional_value', 'weight')
