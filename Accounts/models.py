from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save 
# from django.dispatch import receiver




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField()

    def __str__(self):
        return str(self.user)

 


