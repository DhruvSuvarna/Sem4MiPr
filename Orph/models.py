from django.db import models

# Create your models here.

class Display_Orphanages(models.Model):
    
    name =  models.TextField()
    img =  models.ImageField(upload_to='pics')
    location = models.TextField()
    weblink = models.TextField()
