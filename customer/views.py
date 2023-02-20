#  View level Imports ...
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Importing Models ...
from product.models import Product
from customer.models import AddressDetails
from accounts.models import AbstractBaseUser, Account
from transactions.models import Transaction, TransactionItem

# Custom Imports ...
from FoodMart.mixins import CustomerMixin
from FoodMart.decorators import unauthenticated_user


# Create your views here.
class CustomerRegisterView(View):
    @unauthenticated_user
    def get(self, request):
        return render(request, 'customer/register.html')

    @unauthenticated_user
    def post(self, request):
        email = request.POST.get("email")
        username = request.POST.get("username")
        mobile = request.POST.get("phone")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password")
        if confirm_password == password:
            user = Account(first_name=fname, last_name=lname, username=username, email=email, phone_no=mobile)
            user.set_password(password)
            user.is_vendor = False
            user.is_staff = False
            user.is_superuser = False
            user.is_active = True
            user.is_customer = True
            user.save()
            messages.success(request, "Account has been created!")
            return redirect("customer:login")
        else:
            messages.error(request, "Passwords don't match")
            return redirect("customer:login")


class DashboardView(CustomerMixin, View):
    def get(self, request):
        return render(request, 'customer/dashboard.html')


class HistoryView(CustomerMixin, View):
    def get(self, request):
        return render(request, 'customer/history.html')


class ProfileView(CustomerMixin, View):
    def get(self, request):
        return render(request, 'customer/')