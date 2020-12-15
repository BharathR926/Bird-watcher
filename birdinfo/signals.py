from django.db.models.signals import post_save
from birdlist.models import BirdListings
from django.dispatch import receiver
from.models import Birdinfo

@receiver(post_save,sender=BirdListings)
def post_save_create_userprofile(sender,instance,created,**kwargs):
    if created:
       Birdinfo.objects.create(bird=instance)