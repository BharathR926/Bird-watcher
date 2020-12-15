from django.db.models.deletion import SET_DEFAULT
from user.models import User
from birdlist.models import BirdListings
from django.db import models

# Create your models here.
class Track(models.Model):
   
    bird = models.OneToOneField(BirdListings,default='1',on_delete=models.CASCADE)
    track_1 = models.FileField(upload_to='track/%Y/%m/%d/')
    track_2 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_3 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_4 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_5 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_6 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_7 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    def __str__(self):
         return f"{self.bird.bird_name}"