from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/", views.product, name='product'),
    path('about/', views.about, name='about'),
    path('inventory/', views.inventory, name='inventory'),
    path('order/', views.order, name='order'),
    path('customer/', views.customer, name='customer'),
    path('login/', views.login, name='login'),
    
    path('base', views.base, name='base')
]