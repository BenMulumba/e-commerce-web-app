from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/", views.product, name='product'),
    path('about/', views.about, name='about'),
    path('card/', views.card, name='card'),
    path('order/', views.order, name='order'),
    path('promotion/', views.promotion, name='promotion'),  
    path('base', views.base, name='base')
]