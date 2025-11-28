from django.db import models

# Create your models here.
class Signupdb(models.Model):
    Signup_username=models.CharField(max_length=30,null=True,blank=True)
    Signup_email=models.EmailField(null=True,blank=True)
    Signup_mobile=models.IntegerField(null=True,blank=True)
    Signup_password=models.CharField(max_length=30,null=True,blank=True)
    Signup_confirm=models.CharField(max_length=30,null=True,blank=True)

class Bookingdb(models.Model):
    Booking_firstname=models.CharField(max_length=30,null=True,blank=True)
    Booking_lastname=models.CharField(max_length=30,null=True,blank=True)
    Booking_age=models.IntegerField(null=True,blank=True)
    Booking_gender=models.CharField(max_length=30,null=True,blank=True)
    Booking_address=models.TextField(null=True,blank=True)
    Booking_email=models.EmailField(null=True,blank=True)
    Booking_mobile=models.IntegerField(null=True,blank=True)
    Booking_class=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.Booking_firstname

class Orderdb(models.Model):
    Order_fullname=models.CharField(max_length=30,null=True,blank=True)
    Order_email=models.EmailField(null=True,blank=True)
    Order_phone=models.IntegerField(null=True,blank=True)
    Order_address=models.TextField(null=True,blank=True)
    Order_payment=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.Order_fullname

class Cartdb(models.Model):
    Singlepottery_username=models.CharField(max_length=30,null=True,blank=True)
    Singlepottery_name=models.CharField(max_length=30,null=True,blank=True)
    Singlepottery_price=models.IntegerField(null=True,blank=True)
    Singlepottery_total = models.IntegerField(null=True, blank=True)
    Singlepottery_quantity = models.CharField(max_length=30, null=True, blank=True)
    Singlepottery_image = models.ImageField(upload_to="Cart Images", null=True, blank=True)

    def __str__(self):
        return self.Singlepottery_name