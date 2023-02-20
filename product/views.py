from django import views
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Mixins
from FoodMart.mixins import VendorMixin

# Product Model
from product.models import Product, ProductImage, Category


class AddProductView(VendorMixin, views.View):
    login_url = reverse_lazy('account:login')

    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'vendor/products/add_product.html', context={'categories': categories})

    def post(self, request):
        product = Product()
        product.product_name = request.POST['product_name']
        product.description = request.POST['description']
        product.stock = request.POST['stock']
        product.price = request.POST['price']
        product.is_available = request.POST['is_avaliable']
        product.category_id = request.POST['category']
        product.vendor_id = request.user
        product.save()
        for each in request.FILES.getlist('images'):
            ProductImage(product_id=product, image=each).save()
        messages.success(request, "Product Added")
        return redirect('vendor:list_product')


class ProductListView(VendorMixin, views.View):
    login_url = reverse_lazy('account:login')

    def get(self, request):
        vendor = request.user
        products = Product.objects.filter(vendor_id=vendor).order_by('modified_date')
        return render(request, 'vendor/products/product.html', {'product_object': products})


# Create your views here.
class UpdateProductView(VendorMixin, views.View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        if request.user == product.vendor_id:
            product_images = ProductImage.objects.filter(product_id=product)
            category = Category.objects.all()
            return render(request, 'vendor/products/update_product.html', {'product': product,
                                                                  'categories': category,
                                                                  'productImages': product_images})
        else:
            messages.error("Unauthorized Vendor!")
            return redirect('account:login')

    def post(self, request, id):
        product = Product.objects.get(id=id)
        if product.vendor_id == request.user:
            product.product_name = request.POST['product_name']
            product.price = request.POST['price']
            product.description = request.POST['description']
            product.stock = request.POST['stock']
            product.is_available = request.POST['is_avaliable']
            product.category_id = request.POST['category']
            product.save()
            messages.success(request, "Updated Product", product.product_name)
            return redirect('vendor:list_product')
        else:
            messages.error(request, "Unauthorized Access!")
            redirect('vendor:list_product')


class DeleteProductView(VendorMixin, views.View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        if product.vendor_id == request.user:
            messages.success(request, "Product Removed")
            product.delete()
            return redirect("vendor:list_product")
        else:
            messages.error(request, "Access Denied")
            return redirect('vendor:list_product')