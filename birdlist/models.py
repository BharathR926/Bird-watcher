from django.db import models
from user.models import User
from birdinfo.models import Birdinfo
from audio.models import Track
from image.models import Image

# Create your models here.
class BirdListings(models.Model):
    bird_name = models.CharField(max_length=100)
    info = models.ForeignKey(Birdinfo,on_delete=models.DO_NOTHING)
    uploaded_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    main_image = models.ForeignKey(Image,on_delete=models.DO_NOTHING)
    main_track = models.ForeignKey(Track,on_delete=models.DO_NOTHING)
    def __str__(self):
            return self.bird_name
