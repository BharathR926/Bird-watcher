from user.models import User
from django.db import models
from datetime import datetime
from birdlist.models import BirdListings

# Create your models here.
class Birdinfo(models.Model):
    bird = models.OneToOneField(BirdListings,default='1',on_delete=models.CASCADE)
    comm_Name = models.CharField(max_length=100)
    sci_Name = models.CharField(max_length=100)
    Klass = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=datetime.now)
    wiki_link = models.CharField(max_length=200)
    def __str__(self):
         return f"{self.bird.bird_name}"