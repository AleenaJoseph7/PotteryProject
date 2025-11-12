from django.db import models

# Create your models here.
class catergorydb(models.Model):
    Duration=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.Duration

class productdb(models.Model):
    Product_name=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.Product_name

class potterydb(models.Model):
    Pottery_name=models.CharField(max_length=30,null=True,blank=True)
    Pottery_category=models.CharField(max_length=30,null=True,blank=True)
    Pottery_price=models.IntegerField(null=True,blank=True)
    Pottery_description=models.TextField(null=True,blank=True)
    Pottery_image=models.ImageField(upload_to="Pottery Images",null=True,blank=True)

    def __str__(self):
        return self.Pottery_name