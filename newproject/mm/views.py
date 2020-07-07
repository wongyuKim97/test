from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')

def ii(request):
    return render(request, 'ii.html')

def i2(request):
    return render(request, 'i2.html')
