from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
    
    
def artists(request):
    return render(request,'artists.html')


def artist(request):
    return render(request,'artist.html')
    

def blog(request):
    return render(request,'blog.html')

def login(request):
    return render(request,'login.html')
    
def register(request):
    return render(request,'register.html')
    
def songupload(request):
    return render(request,'songupload.html')