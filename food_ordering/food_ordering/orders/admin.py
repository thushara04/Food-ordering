from django.contrib import admin
from .models import FoodItem,CartItem
# Register your models here.
admin.site.register(FoodItem)
admin.site.register(CartItem)
