from product.models import Category
from django.contrib.admin import ModelAdmin, site


class CategoryAdmin(ModelAdmin):
    prepopulated_fields = {'slug': ('category_name', ), }
    list_display = ['category_name', ]


# Register your models here.
site.register(Category)
