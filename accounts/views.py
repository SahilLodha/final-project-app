# Django Defaults
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

#  Custom Imports
from FoodMart.decorators import unauthenticated_user


class LoginView(View):
    @unauthenticated_user
    def get(self, request):
        print("Here 1")
        return render(request, 'login.html')

    @unauthenticated_user
    def post(self, request):
        print("Here")
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                url = 'vendor:orders' if user.is_vendor else 'customer:dashboard'
                login(request, user=user)
                messages.success(request, "Successfully Logged In.")
                return redirect(url)
            else:
                messages.error("Inactive user cannot login")
                return redirect('account:login')
        else:
            messages.error(request, "User name and password did not match")
            return redirect('account:login')


class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('account:login')

    def get(self, request):
        logout(request)
        return redirect('account:login')
