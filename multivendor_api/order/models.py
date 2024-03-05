from django.db import models
from account.models import User
from product.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # replace User with Customer  # need to add "related_name here"
    products = models.ManyToManyField(Product, through='OrderItem') # OrderItem as below
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)
    order_id= models.CharField(max_length = 50)
    # Add any other relevant fields             ?? when you copy from chatgpt, at least read it


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE) # need to add "related_name here"
    quantity = models.IntegerField()
    data_added = models.DateTimeField()
