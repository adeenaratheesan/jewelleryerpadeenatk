from django.db import models

from admins.models import Product
from home.models import Customer

# Create your models here.
class Mycart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.BigIntegerField()
    