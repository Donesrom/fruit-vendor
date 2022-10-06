from django.shortcuts import render
from .models import *


def index(request):
    gen_products = Gen.objects.all()
    featured_products = Product.objects.filter(featured=True)
    
    context = {
        'gen_products' : gen_products,
        'featured_products' : featured_products,
    }
    return render(request, "index.html", context)

def shop(request):
    shop_products= Product.objects.all()

    context = {
        'shop_products' : shop_products
    }
    return render(request, "shop.html", context)


def wishlist(request):
    return render(request, "wishlist.html")

def checkout(request):
    return render(request, "checkout.html")

def cart(request):
    return render(request, "cart.html")

def contact(request):
    return render(request, "contact.html")