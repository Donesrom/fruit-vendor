from multiprocessing import context
import django
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from .models import *

#customer = UserProfile.objects.create(user = request.user)

#@login_required(login_url= "login")
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
        orderitems = order.orderitem_set.all()
    else:
        orderitems = []
        order = {"get_cart_total":0 , "get_cart_items":0}

    context= {'items':orderitems, 'order': order}
    return render(request, 'cart.html', context)


def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk)
    order_item, created = OrderItem.objects.get_or_create(
        product = product,
        user = request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("core:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("core:order-summary")
        
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("core:order-summary")

def add_to_wishlist(request):
    pass 

def buy_now(request):
    pass



@login_required(login_url="login")
def wishlist(request):
    items = Wishlist.objects.all()
    
    context = {
        'items' : items
    }

    return render(request, "wishlist.html", context)

def checkout(request):
    return render(request, "checkout.html")