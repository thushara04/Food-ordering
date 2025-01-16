from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price =models.FloatField()
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.food_item.name}"