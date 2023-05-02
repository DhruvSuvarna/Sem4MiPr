from django.db import models
# Create your models here.
class Orphanage_Display(models.Model):
    
    username = models.CharField(max_length=150, unique=True, default='dhruv')
    name =  models.TextField()
    img =  models.ImageField(upload_to='pics')
    location = models.TextField()
    weblink = models.TextField()

class Suggestions(models.Model):
    
    username = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    name =  models.CharField(max_length=150)
    email = models.EmailField()
    suggestion = models.TextField()