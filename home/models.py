from django.db import models

# Create your models here.
class Customer(models.Model):

    image=models.ImageField(upload_to='customer')
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=25)
    e_mail=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    password=models.CharField(max_length=25)
    
    
    
    class Meta:
        db_table='customer' 


class Seller(models.Model):
    # seller_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    mobile=models.CharField(max_length=20)
    e_mail=models.CharField(max_length=100)
    company_logo=models.ImageField(upload_to='seller/')
    bank_name=models.CharField(max_length=150)
    acc_name=models.CharField(max_length=150)
    accc_no=models.BigIntegerField()
    ifsc=models.CharField(max_length=150)
    branch_name=models.CharField(max_length=500)
    Username=models.CharField(max_length=100)
    password=models.CharField(max_length=16)

    class Meta:
        db_table='seller'
 

