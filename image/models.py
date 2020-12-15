from user.models import User
from django.db import models
from birdlist.models import BirdListings

# Create your models here.
class Image(models.Model):
    bird = models.OneToOneField(BirdListings,default='1',on_delete=models.CASCADE)
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
         return f"{self.bird.bird_name}"