from django import views
from django.views.generic import ListView
from django.contrib import messages

# Redirection Imports
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Mixins: Django Default
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

# Custom Mixins and Decorators
from FoodMart.mixins import VendorMixin
from FoodMart.decorators import unauthenticated_user

# Model Import
from transactions.models import TransactionItem


class OrderListView(VendorMixin, ListView):
    login_url = reverse_lazy('account:login')
    model = TransactionItem
    template_name = 'vendor/order.html'
    paginate_by = 20
    http_method_names = ['get']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(product__vendor_id=self.request.user).filter(status=1)


class ChangeStatusDelivered(LoginRequiredMixin, views.View):
    def get(self, request, id):
        item = TransactionItem.objects.get(id=id)
        if item.product.vendor_id == request.user:
            item.status = 2
            item.save()
            messages.success(request, "Item Delivered.")
            return redirect('vendor:delivery')
        else:
            messages.info(request, "User Access Denied")
            return redirect('vendor:orders')


class DeliveredListView(LoginRequiredMixin, views.View):
    login_url = reverse_lazy('account:login')

    def get(self, request):
        if request.user.is_vendor:
            items = TransactionItem.objects.filter(product__vendor_id=request.user).filter(status=2)
            return render(request, 'vendor/delivery.html', {"items": items})
        else:
            messages.error(request, 'Not a Vendor')
            return redirect('store:home')


class VendorProfile(LoginRequiredMixin, views.View):
    login_url = reverse_lazy('account:login')

    def get(self, request):
        if request.user.is_vendor:
            return render(request, 'vendor/profile.html')
        else:
            logout(request)
            return redirect('account:login')

    def post(self, request):
        if request.user.is_vendor:
            user = request.user
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.user_name = request.POST['username']
            user.phone_no = request.POST['phone_no']
            user.email = request.POST['email']
            user.save()
            logout(request)
            messages.success(request, "User Updated, Logged Out!");
            return redirect('account:login')
        else:
            return redirect('account:login')
