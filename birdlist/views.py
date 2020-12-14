from django.shortcuts import render


def index(request):
    return render(request,'birdlisting/many.html')

def individualbird(request):
    return render(request,'birdlisting/one.html')

