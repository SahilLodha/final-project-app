from django.urls import path
from customer import views

app_name = 'customer'

urlpatterns = [
    # path('base/', views.CustomerBaseView.as_view(), name='base'),
    # path('', views.OrderView.as_view(), name='dashboard'),
    # path('login/', views.CustomerLoginView.as_view(), name='login'),
    # path('profile', views.CustomerProfile.as_view(), name='profile'),
    # path('logout/', views.CustomerLogoutView.as_view(), name='logout'),
    path('register/', views.CustomerRegisterView.as_view(), name='register'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('history/', views.HistoryView.as_view(), name='history'),
    path('recommendation/', views.RecommendationView.as_view())
    # path('profile/address/', views.CustomerAddress.as_view(), name="address_add"),
    # path('featured/<str:code>/', views.CustomerFeaturedView.as_view(), name='featured'),
    # path('profile/remove/address/<int:id>', views.AddressModifyView.as_view(), name="modify_address"),
]