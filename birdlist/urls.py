from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='birdlist'),
    path('<int:individualbird_id>',views.individualbird,name='individualbird'),
   
]
