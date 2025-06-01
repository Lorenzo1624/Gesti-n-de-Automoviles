from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import models 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_vendor_profile(sender, instance, created, **kwargs):
    if created:
        from .models import Vendor
        Vendor.objects.create(user=instance)