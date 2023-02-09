from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from FoodMart import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendor/', include('vendor.urls')),
    path('customer/', include('customer.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, kwargs={'document_root': settings.MEDIA_ROOT})
]
