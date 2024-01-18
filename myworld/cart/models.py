from django.db import models
from django.contrib.auth.models import User
from dog.models import Dogproduct


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dproduct = models.ForeignKey(Dogproduct,on_delete=models.CASCADE)  
    dproduct_qty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150,null=False)
    email = models.CharField(max_length=150,null=False)
    address = models.TextField(null=False)
    state = models.CharField(max_length=150,null=False)
    city = models.CharField(max_length=150,null=False)
    phone = models.CharField(max_length=150,null=False)
    zip = models.CharField(max_length=150,null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150,null=False)
    payment_id = models.CharField(max_length=250,null=True)
    orderstatuses = (
        ('Pending','Pending'),
        ('Out for Shipping','Out of Shipping'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=150,choices=orderstatuses,default='Completed')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{} - {}'.format(self.id,self.tracking_no)



class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Dogproduct,on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self) -> str:
        return '{} {}'.format(self.order.id,self.order.tracking_no)


    
class Pay(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nameoncard = models.CharField(max_length=150,null=False,default=__name__)
    cardno =  models.CharField(max_length=20,null=False,default=1111222233334444)
    month = models.CharField(max_length=20,null=False,default='September')
    year = models.CharField(max_length=20,null=False,default='2020')
    cvv =  models.CharField(max_length=20,null=False,default='234')
    
    