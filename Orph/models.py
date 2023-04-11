import uuid
from django.db import models
from Orphanage.models import Orphanage_Details
# Create your models here.
class Orphanage_Display(models.Model):
    
    username = models.CharField(max_length=150, unique=True, default='dhruv')
    name =  models.TextField()
    img =  models.ImageField(upload_to='pics')
    location = models.TextField()
    weblink = models.TextField()