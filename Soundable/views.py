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