from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=255, primary_key = True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=10)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=2, default ='C')
    
class Product(models.Model):
    productid = models.IntegerField(primary_key = True)
    pname = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    specifications = models.CharField(max_length=255)
    image = models.CharField(max_length=255, default="")
    rating = models.FloatField(default=3.5)

# id is auto-generated and incremented by django
class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    orderdate = models.DateTimeField(auto_now_add = True)
    paidstatus = models.BooleanField(default=False)
    finalprice = models.IntegerField()

class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder, on_delete = models.CASCADE)
    invoice_number = models.CharField(max_length = 255)
    item = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    qty = models.IntegerField()
    price = models.IntegerField()
    total = models.IntegerField()

# promo code is of 5 letters
#auto generated id == primary key
class Cart(models.Model):
    productlist = models.CharField(max_length=255)
    promocode = models.CharField(max_length=5)
    
    
    
