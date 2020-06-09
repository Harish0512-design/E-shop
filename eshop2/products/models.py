from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils.datetime_safe import datetime
from datetime import timedelta
from django.core.validators import RegexValidator

# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length=100)
    p_price = models.FloatField()
    p_date = models.DateTimeField(auto_now_add=True)
    p_des = models.TextField()
    p_img = models.ImageField(upload_to="images")
    p_instock = models.IntegerField(default=1)
    def __str__(self):
        return "%s (%s)" % (self.p_name, self.p_date)

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="images",null=True)
    gender = models.CharField(max_length=100,choices=(('male','male'),('female','female'),('others','others')))
    phone = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=15)
    hno = models.CharField(max_length=100)  
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    dist = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    user_register_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s (%s)" % (self.user, self.name)
    
class Sold(models.Model):
    user = models.ForeignKey(to=User,on_delete=CASCADE)
    p_name = models.CharField(max_length=100)
    p_price = models.FloatField()
    p_img = models.ImageField(upload_to="images")
    p_quantity = models.IntegerField(null=True,default=1)
    amount = models.FloatField(null=True,blank=True)
    p_instock = models.IntegerField(default=1)
    sold_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s' %(self.p_name)
    
class Deliver(models.Model):
    products = models.ManyToManyField(Sold)
    name = models.ForeignKey(to=User,on_delete=CASCADE)
    cust_name = models.CharField(max_length=100)
    phone = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")],max_length=15)
    hno = models.CharField(max_length=100)  
    street = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    dist = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    sold_on = models.DateTimeField(auto_now_add=True)  
    delivered_on = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return '%s' %(self.name)


class Cart(models.Model):
    product = models.CharField(max_length=100)
    p_name = models.CharField(max_length=100)
    p_price = models.FloatField()
    p_img = models.ImageField(upload_to="images")
    p_quantity = models.IntegerField(null=True,default=1)
    amount = models.FloatField(default=0)
    p_instock = models.IntegerField(default=1)
    def __str__(self):
        return "%s (%s)" % (self.product, self.p_name)
    

    
