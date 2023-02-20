from django import views
from django.contrib import messages
from django.views import View
from category.forms import CategoryForm

from django.views import View
from django.urls import reverse_lazy
from FoodMart.mixins import VendorMixin
from django.shortcuts import redirect, render
from django.db import models

from product.models import Product, Category


class AddCategory(VendorMixin, View):
    login_url = reverse_lazy('vendor:login')

    def get(self, request):
        return render(request, 'vendor/category/add_category.html')

    def post(self, request):
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Category created.")
            return redirect('vendor:categories')

        return redirect('vendor:categories')


class UpdateCategory(VendorMixin, View):
    login_url = reverse_lazy('vendor:login')

    def get(self, request, id):
        category = Category.objects.first(id=id)
        return render(request, 'vendor/category/update_category.html', {'category': category})

    def post(self, request):
        pass


class ListCategory(VendorMixin, View):
    login_url = reverse_lazy('vendor:login')

    def get(self, request):
        categories = Category.objects.all()
        print(categories)
        return render(request, 'vendor/category/category.html', {'categories': categories})


class RemoveCategory:
    def post(self, request):
        pass
