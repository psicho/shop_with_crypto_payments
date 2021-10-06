from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from vanilla import CreateView, DeleteView, DetailView, ListView, UpdateView
from .models import Category, Product
from cart.forms import CartAddProductForm


class ProductListView(ListView):
    template_name = "shop/product/product_list.html"
    model = Category
    context_object_name = 'category1'

    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     return self.render_to_response(context)

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()

        if self.kwargs.get('category_slug'):
            category_slug = self.kwargs['category_slug']
            category = Category.objects.get(slug=category_slug)
            products = Product.objects.filter(available=True, category=category)
        else:
            products = Product.objects.filter(available=True)
            category = None

        context = {
            'products': products,
            'categories': categories,
            'category': category,
        }

        return context

    def get_queryset(self):
        if self.kwargs.get('category_slug'):
            res = Product.objects.filter(available=True,
                                         category=Category.objects.filter(slug=self.kwargs.get('category_slug')))
        else:
            res = Product.objects.filter(available=True)
        return res


class ProductDetailView(DetailView):
    template_name = "shop/product/product_detail.html"

    def get(self, request, *args, **kwargs):
        queryset = (Product.objects
                    .filter(id=kwargs['id'],
                            slug=kwargs['slug']))
        product = get_object_or_404(queryset)
        cart_product_form = CartAddProductForm()
        context = self.get_context_data(product, cart_product_form)

        return self.render_to_response(context)

    def get_context_data(self, product: Product, cart_product_form: CartAddProductForm(), **kwargs):

        context = {
            'product': product,
            'cart_product_form': cart_product_form,
            # 'categories': categories,
            # 'category': category,
        }
        return context

