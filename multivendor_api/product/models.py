from django.db import models
from account.models import User

class Product(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.CharField(max_length=255)  
    product_image = models.ImageField(upload_to='product_images/')  
    category = models.CharField(max_length=50)  
