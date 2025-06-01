from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    def __str__(self):
        return self.username
    pass 

class Vendor (models.Model):
    contact = models.CharField(max_length=100)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='vendor')

    def __str__(self):
        return f"{self.user.username}"


class Car(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    published_date = models.DateTimeField(auto_now_add=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=500)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name