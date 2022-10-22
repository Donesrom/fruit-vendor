from django.urls import path, include
from .views import *

urlpatterns = [
    
    path('cart', cart, name='cart'),
    path('wishlist', wishlist, name='wishlist'),
    path('checkout', checkout, name='checkout'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    
 
]