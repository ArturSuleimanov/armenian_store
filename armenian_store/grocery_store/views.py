from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView
from .models import Product
from django.db.models import Q

# Create your views here.
class ProductListPage(ListView):
    model = Product
    template_name = "grocery_store/product_list.html"
    context_object_name = 'products'
    paginate_by = 15

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
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
        object_list = Product.objects.filter(
            Q(name__iregex=query) | Q(description__iregex=query)
        ).order_by('-time_create')
        return object_list


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Результаты поиска'
        context['search_by'] = self.request.GET.get('search-input-main')
        return context