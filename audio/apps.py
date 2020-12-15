from django.apps import AppConfig


class AudioConfig(AppConfig):
    name = 'audio'
    def ready(self):
           import audio.signals
   
   
