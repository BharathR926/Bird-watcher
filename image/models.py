from user.models import User
from django.db import models

# Create your models here.
class Image(models.Model):
    Image_name = models.CharField(max_length=100,blank=True)
    uploaded_by= models.ForeignKey(User,on_delete=models.DO_NOTHING)
    image_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    image_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    image_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.Image_name