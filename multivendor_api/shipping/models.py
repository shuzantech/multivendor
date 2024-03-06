from django.db import models
from order.models import Order

# Create your models here.
class Shipping(models.Model):
    STATUS_CHOICES = (
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    )


    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=50)