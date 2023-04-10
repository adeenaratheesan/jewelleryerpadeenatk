from django.db import models

from home.models import Seller

# Create your models here.
class Admins(models.Model):

    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    
    
    
    class Meta:
        db_table='admins' 

class Category(models.Model):
    Category_name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    
    # neck_style=models.CharField(max_length=200)


    class Meta:
        db_table='category'


class Type(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    type=models.CharField(max_length=200)
   
   
    class Meta:
        db_table='type'



class Style(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    type= models.ForeignKey(Type,on_delete=models.CASCADE)
    style=models.CharField(max_length=200)

    class Meta:
        db_table='style'


class Product(models.Model):    
    category = models.CharField(max_length = 30, default='')
    type=models.CharField(max_length=200)
    style=models.CharField(max_length=200,default='')
    p_name=models.CharField(max_length=50)
    p_number=models.CharField(max_length=20)
    description=models.CharField(max_length=500)
    p_stock=models.BigIntegerField()
    p_price=models.FloatField()
    p_image=models.ImageField(upload_to='product/')

    class Meta:
        db_table='product' 
   
