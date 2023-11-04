from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart_delete', views.cart_delete, name='cart_delete'),
    path('cart_update', views.cart_update, name='cart_update')

]
