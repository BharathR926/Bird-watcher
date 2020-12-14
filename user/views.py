from django.http import request
from django.shortcuts import render,redirect

# Create your views here.
def login_signup(request):
    return render(request,'accounts/login_signup.html')

def logout(request):
    return redirect('home')