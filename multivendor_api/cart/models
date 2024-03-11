from django.db import models
from customer.models import Customer
from product.models import Product

class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE) # need to add "related_name here"
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()


