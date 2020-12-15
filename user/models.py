from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class UserProfile(models.Model):
    
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    dob = models.DateField
    country = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
   
    def __str__(self):
        return f"{self.user.username}-{self.is_verified}"