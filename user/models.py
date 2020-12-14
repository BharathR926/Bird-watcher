from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    dob = models.DateField
    email = models.EmailField
    country = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.user_name