from django.urls import path

# Importing Views
from vendor import views
from category.views import AddCategory, ListCategory, UpdateCategory
from product.views import AddProductView, UpdateProductView, DeleteProductView, ProductListView

app_name = 'vendor'
urlpatterns = [
    # Auth Routes ...
    path('profile/', views.VendorProfile.as_view(), name='vendor_profile'),

    # Order and Delivery Routes ...
    path('', views.OrderListView.as_view(), name='orders'),
    path('delivery/', views.DeliveredListView.as_view(), name='delivery'),
    path('delivery/<int:id>', views.ChangeStatusDelivered.as_view(), name="change_status"),

    # Category Paths ...
    path('category/', ListCategory.as_view(), name='categories'),
    path('add/category/', AddCategory.as_view(), name='add_category'),
    path('edit/<int:slug>/category/', UpdateCategory.as_view(), name='update_category'),

    # Product Path ...
    path('add/product/', AddProductView.as_view(), name='add_product'),
    path('list/product', ProductListView.as_view(), name='list_product'),
    path('edit/<int:id>/product/', UpdateProductView.as_view(), name='update_product'),
    path('delete/product/<int:id>/', DeleteProductView.as_view(), name='delete_product'),
]

