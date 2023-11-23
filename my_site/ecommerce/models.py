from django.db import models

# Create your models for customer.
class customer (models.Model):
    name= models.CharField(max_length=255)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)
    product= models.CharField(max_length=255)


class product (models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    quantity_stk= models.IntegerField()
    price= models.CharField(max_length=50)
    manufacturer= models.CharField(max_length=50)
    released_date= models.DateField()
    # adding models for modify,delete, selest

class order(models.Model):
    order_number= models.IntegerField()
    item = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    customer =models.CharField(max_length=100)

# class user(models.Model):


