from django.db import models
from account.models import User
# Create your models here.
class Payment(models.Model):
    user =models.ForeignKey(User, related_name="users_payment",on_delete =models.CASCADE )# need to add "related_name here"
    amount = models.FloatField()
    transaction_id =models.CharField(max_length=15)
    paid_status =models.BooleanField(default=False)

