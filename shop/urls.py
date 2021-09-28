from django.urls import path
from shop.views import ProductListView

app_name = 'shop'

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('<slug:category_slug>/', ProductListView.as_view(), name="product_list_by_category"),
]