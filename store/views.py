from django.core.paginator import Paginator
from django.views import View
from django.shortcuts import render
from product.models import Product
from django.views.generic import ListView


class HomeView(View):
    def get(self, request):
        latest = Product.objects.order_by('-created_date')
        return render(request, 'store/home.html', {'latest': latest})


class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        latest = Product.objects.order_by('-created_date')
        return render(request, 'store/productDetail.html', {'product': product, 'latest': latest})


class CartView(View):
    def get(self, request):
        return render(request, 'store/cart.html')


class ShopView(ListView):
    model = Product
    template_name = 'store/shop.html'
    paginate_by = 40
    http_method_names = ['get']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_available=True)