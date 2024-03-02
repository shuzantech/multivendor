from django.db import models
from account.models import User
# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User , on_delete=models.CASCADE)
	date_of_birth = models.DateField() # as this data is not there in User Model
	no_of_orders = models.IntegerField() # you may give discounts based on this


class Vendor(models.Model):
	user = models.OneToOneField(User , on_delete=models.CASCADE)
	no_of_product = models.IntegerField()
