from django.db import models


# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=25)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=8)

class Product(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    productname=models.CharField(max_length=20)
    details=models.CharField(max_length=50)

class cart(models.Model):
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    
