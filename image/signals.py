from django.db.models.signals import post_save
from birdlist.models import BirdListings
from django.dispatch import receiver
from.models import Image

@receiver(post_save,sender=BirdListings)
def post_save_create_userprofile(sender,instance,created,**kwargs):
    if created:
        Image.objects.create(bird=instance)