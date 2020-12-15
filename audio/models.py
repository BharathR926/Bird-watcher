from user.models import User
from django.db import models

# Create your models here.
class Track(models.Model):
    Track_name = models.CharField(max_length=100,blank=True)
    uploaded_by= models.ForeignKey(User,on_delete=models.DO_NOTHING)
    track_1 = models.FileField(upload_to='track/%Y/%m/%d/')
    track_2 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_3 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_4 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_5 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_6 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    track_7 = models.FileField(upload_to='track/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.Track_name