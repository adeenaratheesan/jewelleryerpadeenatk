from django.db import models
from datetime import date

from admins.models import Product
from home.models import Customer

# Create your models here.
class Mycart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.BigIntegerField()
    

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount=models.FloatField()
    status= models.CharField(max_length=20,default="pending")
    provider_order_id = models.CharField(max_length=40)
    payment_id = models.CharField(max_length=36)
    signature_id = models.CharField(max_length=128)

    class Meta:
        db_table = 'order_tb'

class Order_detail(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=20,default="pending") #update after payment confirmed
    payment_type = models.CharField(max_length=20)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)


    class Meta:
        db_table = 'order_detail'