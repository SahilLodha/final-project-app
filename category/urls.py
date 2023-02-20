from django.urls import path
from category import views

app_name = 'category'

urlpatterns = [
    path('get/subcategory/<int:id>/', views.PassSubCategoriesJSON.as_view()),
]
