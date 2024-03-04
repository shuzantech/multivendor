from django.db import models

# Create your models here.
# Product model :
#     title = CharField()
#     selling_price = FloatField()
#     discount_price = FloatField()
#     description = CharField
#     product_image = ImageField()
#     category = CharField()

class Product(models.Model):
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    actual_price = models.FloatField()
    description = models.CharField(max_length = 500) 
    product_image = models.ImageField(upload_to= "product_image")
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    