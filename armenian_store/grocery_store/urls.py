from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListPage.as_view(), name = "product_list"),
    path('search/', SearchResultsView.as_view(), name = 'search'),
    path('product/<int:product_id>', ProductPage.as_view(), name='product_page'),
    path('about_us/', about_us, name = "about_us"),
    path('contacts/', contacts, name="contacts"),
    path('feedbacks/', feedbacks, name="feedbacks"),
    path('category/<int:category_id>', ShowProductByCategory.as_view(), name = "product_by_category"),
    path('categories/', CategoriesListPage.as_view(), name="categories")
]

