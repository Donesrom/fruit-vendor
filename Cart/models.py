from email.policy import default
from itertools import product
from pickle import TRUE
from django.db import models
from Veggie.models import Product
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()



class Customer(models.Model):
    username = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    created_at = models.DateTimeField(default = datetime.now)
    ordered = models.BooleanField(default = False)
    quantity = models.IntegerField(default = 1)
    total = models.IntegerField(default = 0)

    def __str__(self):
        return self.product

    @property
    def total(self):
        return self.quantity * self.total


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.SET_NULL, null = True)
    created_at = models.DateTimeField(default = datetime.now)
    complete = models.BooleanField(default = False)
    transaction_id=models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
    print(customer)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.order)
 
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class CheckoutDetail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    total_amount = models.CharField(max_length=10, blank=True,null=True)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.address