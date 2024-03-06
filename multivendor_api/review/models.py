from django.db import models
from account.models import User
from product.models import Product

class Review(models.Model):
    RATING_CHOICES = (
        (1, 'Poor'),
        (2, 'Fair'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
