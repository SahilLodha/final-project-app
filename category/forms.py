from django.forms import ModelForm
from product.models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description', 'image']