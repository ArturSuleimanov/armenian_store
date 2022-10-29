from django.shortcuts import render
from django.views.generic import ListView

from .forms import ProductForm
from .models import Product, Category
from django.db.models import Q
from django.forms.models import model_to_dict
from itertools import chain


# Create your views here.
class ProductListPage(ListView):
    model = Product
    template_name = "grocery_store/product_list.html"
    context_object_name = 'products'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список продуктов'
        context['search_by'] = ""
        return context


    def get_queryset(self, *args, **kwargs):
        return Product.objects.order_by('-time_create')


class SearchResultsView(ListView):
    '''
    Поиск пользователей по имени и фамилии
    '''
    paginate_by = 15
    model = Product
    template_name = 'grocery_store/product_list.html'
    context_object_name = 'products'


    def get_queryset(self):
        """
        Обработка поискового запроса
        """
        query = self.request.GET.get('search-input-main')
        if not query:
            return Product.objects.order_by('-time_create')
        cat_list = Category.objects.filter(Q(title__iregex=query))
        object_list = Product.objects.filter(
            Q(title__iregex=query) | Q(description__iregex=query)
        ).order_by('title')
        for cat in cat_list:
            object_list = list(chain(object_list, Product.objects.filter(category=cat)))
        return object_list


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['category'] = 'Результаты поиска'
        context['search_by'] = self.request.GET.get('search-input-main')
        return context





class ProductPage(ListView):
    model = Product
    template_name = "grocery_store/product_page.html"


    def get_context_data(self, *, object_list=None, **kwargs):
        product_id = self.kwargs.get('product_id')
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(pk = product_id)
        context['product'] = product
        context['title'] = f'{product.title}'
        context['product_form'] = zip(ProductForm(data=model_to_dict(product)), ("Описание", "Состав", "Пищевая ценность", "Масса"))
        return context


class ShowProductByCategory(ListView):
    model = Product
    template_name = "grocery_store/product_list.html"
    context_object_name = 'products'


    def get_queryset(self):
        """
        Обработка поискового запроса
        """
        query = self.kwargs.get('category_id')
        print(query, " !!!!!!++++++++++++++++++++++++++")
        object_list = Product.objects.filter(category=query).order_by('title')
        return object_list




    def get_context_data(self, *, object_list=None, **kwargs):
        category_id = self.kwargs.get('category_id')
        context = super().get_context_data(**kwargs)
        context['title'] = f'{Category.objects.get(pk=category_id)}'
        return context




class CategoriesListPage(ListView):
    model = Category
    template_name = "grocery_store/category_list.html"
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список категорий'
        return context


    def get_queryset(self, *args, **kwargs):
        return Category.objects.order_by('title')



def about_us(request):
    return render(request, 'grocery_store/about_us.html', {"title": "О нас"})

def contacts(request):
    return render(request, 'grocery_store/contacts.html', {"title": "Контакты"})

def feedbacks(request):
    return render(request, 'grocery_store/feedbacks.html', {"title": "Отзывы"})