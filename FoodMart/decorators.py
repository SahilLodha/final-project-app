from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_function(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            url = 'vendor:orders' if request.user.is_vendor else 'customer:dashboard'
            return redirect(url)

        return view_func(self, request, *args, **kwargs)

    return wrapper_function
