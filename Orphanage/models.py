import uuid
from django.db import models
# Create your models here.

class Orphanage_Details(models.Model):
    
    o_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True, default='dhruv')
    o_name =  models.CharField(max_length=100, unique=True)
    o_img =  models.ImageField(upload_to='pics')
    o_state =  models.CharField(max_length=100)
    o_city =  models.CharField(max_length=100)
    o_district =  models.CharField(max_length=100)
    o_address = models.TextField()
    o_weblink = models.TextField()