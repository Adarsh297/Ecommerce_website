from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer(models.Model):
    User=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)

class product(models.Model):
    name=models.CharField(max_length=100,null=True)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True,blank=True)
    image=models.ImageField(null=True,blank=True)


class order(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    
    def get_cart_total(self):
            orderitems = self.orderitem_set.all()
            total= sum([item.get_total for item in orderitems])
            return total 
            
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 


class OrderItem(models.Model):
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def get_total(self):
        total=self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
