from django.apps import AppConfig


class BirdinfoConfig(AppConfig):
    name = 'birdinfo'
    def ready(self):
           import birdinfo.signals
