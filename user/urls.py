from django.urls import path
from .import views

urlpatterns = [
    path('login_signup',views.login_signup,name='login_signup'),
    path('logout',views.logout,name='logout')
   
]
