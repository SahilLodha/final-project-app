from django.urls import path
from store.views import *

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
]