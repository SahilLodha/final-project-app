from django.views import View
from django.shortcuts import render


class BaseView(View):
    def get(self, request):
        return render(request, 'store/base.html')