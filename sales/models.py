from django.db import models
from inventory.models import Sticker

class Order(models.Model):
    sticker = models.ForeignKey(Sticker, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.sticker.name}"
