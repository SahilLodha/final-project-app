from django.urls import path
from store.views import *

urlpatterns = [
    path('', BaseView.as_view(), name='home')
]