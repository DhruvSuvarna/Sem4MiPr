from django.db import models

# Create your models here.
class UtilityDonation(models.Model):
    
    donorname = models.CharField(max_length=150, default='rajat')
    orphanageusername = models.CharField(max_length=150, default='O1')
    orphanagename = models.TextField()
    money = models.IntegerField()
    grains_no = models.FloatField()
    grains =  models.CharField(max_length=150)
    books_no = models.IntegerField()
    books = models.CharField(max_length=150)

class ServiceDonation(models.Model):
    
    donorname = models.CharField(max_length=150, default='rajat')
    orphanageusername = models.CharField(max_length=150, default='O1')
    orphanagename = models.TextField()
    service =  models.CharField(max_length=150)
    mobile = models.BigIntegerField()

class DonorProfile(models.Model):
    
    username = models.CharField(max_length=150, unique=True, default='rajat')
    name = models.CharField(max_length=150, default='rajat')
    profile_pic =  models.ImageField(upload_to='pics')
    mobile = models.BigIntegerField()
    location = models.CharField(max_length=150)