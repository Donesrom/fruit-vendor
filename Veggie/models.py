from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class Gen(models.Model):
    title = models.CharField(max_length= 30)
    image = models.ImageField(upload_to = 'pics')


    def __str__(self):
        return self.title


class Featured(models.Model):
    image = models.ImageField(upload_to = 'pics') 
    title = models.CharField(max_length= 30)
    percent_discount = models.IntegerField()
    price_dc = models.IntegerField()
    price_sale = models.IntegerField()
 


    def __str__(self):
        return self.title

class Shop(models.Model):
    image = models.ImageField(upload_to = 'pics') 
    title = models.CharField(max_length= 30)
    percent_discount = models.IntegerField()
    price_dc = models.IntegerField()
    price_sale = models.IntegerField()
 


    def __str__(self):
        return self.title
