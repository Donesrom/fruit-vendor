from ast import Not
from distutils.command.upload import upload
from django.db import models
from django.db.models.fields.related import OneToOneField


class Product(models.Model):
    title = models.CharField(max_length= 30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pics')     
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=False) #selling price
    percent_discount = models.IntegerField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def discount(self):
        return int(self.discounted_price - self.price)

    @property
    def percent_discount(self):
        return int((self.discount/self.price) * 100)
        

class Gen(models.Model):
    title = models.CharField(max_length= 30)
    image = models.ImageField(upload_to = 'pics')

    def __str__(self):
        return self.title


# class Featured(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price_dc = models.IntegerField() #price discount 
#     price_sale = models.IntegerField()
#     percent_discount = models.IntegerField()

#     def __str__(self):
#         return self.title


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
            return self.title
