from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Category, Product


class ProductListView(ListView):
    template_name = "shop/product/product_list.html"

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        product = Product.objects.filter(available=True)
        category_slug = kwargs.get('category_slug')

        if category_slug:
            pass

        context = {
            'product': product,
            'category': categories
        }
        return context

    def get_queryset(self):
        return Product.objects.all()
