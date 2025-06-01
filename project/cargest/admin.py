from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Car, Vendor

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields = ["name", "published_date", "price", "vendor", "description"]

@admin.register(Vendor)
class vendorAdmin(admin.ModelAdmin):
    fields = ["name", "contact"]

admin.site.register(CustomUser, UserAdmin)