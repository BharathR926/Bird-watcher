from django.db import models
from user.models import User




# Create your models here.
class BirdListings(models.Model):
    bird_name = models.CharField(max_length=100)
   
   
    def __str__(self):
            return self.bird_name
