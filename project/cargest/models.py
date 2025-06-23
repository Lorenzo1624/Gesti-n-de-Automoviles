from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

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
    address = models.TextField()
    latitude = models.FloatField(
        verbose_name="Latitud",
        null=True,
        blank=True,
        help_text="Valor entre -90 y 90"
    )
    longitude = models.FloatField(
        verbose_name="Longitud", 
        null=True,
        blank=True,
        help_text="Valor entre -180 y 180"
    )
    
    def clean(self):
        if (self.latitude is None) != (self.longitude is None):
            raise ValidationError("Debe proporcionar ambas coordenadas o ninguna")
        
        if self.latitude and not (-90 <= self.latitude <= 90):
            raise ValidationError("Latitud debe estar entre -90 y 90")
            
        if self.longitude and not (-180 <= self.longitude <= 180):
            raise ValidationError("Longitud debe estar entre -180 y 180")
        
    def __str__(self):
        return self.name
    
    def get_location(self):
        if self.latitude and self.longitude:
            return [self.latitude, self.longitude]
        return None