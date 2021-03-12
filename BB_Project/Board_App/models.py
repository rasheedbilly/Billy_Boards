from django.db import models

# Create your models here.

class Stock(models.Model):
    ID = models.IntegerField()
    Minimum = models.IntegerField()
    Maximum = models.IntegerField()

class Product(models.Model):
    ID = models.IntegerField()
    Stock.ID = models.IntegerField()
    Name = models.CharField(max_length=30)
    Price = models.DecimalField(max_digits=2)
    Description = models.CharField(max_length=30)
    Image_path = models.CharField(max_length=30)
    Quanity = models.IntegerField()

class Cart(models.Model):
    ID = models.IntegerField()
    #User.ID = models.IntegerField()
    Product.ID = models.IntegerField()
    created = models.DateField()
    total = models.DecimalField(max_digits=2)

class Address(models.Model):
    ID = models.IntegerField()
    Addr = models.IntegerField()
    Unit = models.IntegerField()
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=2)
    Zip = models.IntegerField()
    PO_Box = models.IntegerField()

class User(models.Model):
    ID = models.IntegerField()
    Address.ID = models.IntegerField()
    Cart.ID = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=30)
    member_since = models.DateField()

class Order(models.Model):
    ID = models.IntegerField()
    User.ID = models.IntegerField()
    Cart.ID = models.IntegerField()
    Order_made = models.DateField()
    Order_shipped = models.DateField()
    Order_paid = models.DateField()
    status = models.CharField(max_length=30)



