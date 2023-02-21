from django.views import View
from django.shortcuts import render
from product.models import Product


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
