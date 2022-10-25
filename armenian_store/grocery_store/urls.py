from django.conf.urls.static import static
from django.urls import path

from armenian_store import settings
from .views import *

urlpatterns = [
    path('', ProductListPage.as_view(), name = "product_list"),
    path('search/', SearchResultsView.as_view(), name = 'search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)