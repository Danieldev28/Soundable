from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from Soundable.forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from Soundable.models import *


# Create your views here.

def index(request):
    return render(request,'index.html')

def contact_us(request):
    """Contact submission form to database"""
    if request.method == "POST":
        print(request.POST.get('form'))
        if request.POST.get('form') == 'contact':
             u_contact = contact()
             u_contact.name = request.POST.get('name')
             u_contact.email = request.POST.get('email')
             u_contact.subject = request.POST.get('subject')
             u_contact.messages = request.POST.get('message')
             u_contact.save()
        else:
             subscribe = subscriber()
             subscribe.email = request.POST.get('newsletter')
             subscribe.save()
    
    return render(request,'contact.html')
    
    
def artists(request):
    return render(request,'artists.html')


def artist(request):
    return render(request,'artist.html')
    

def blog(request):
    return render(request,'blog.html')


def register(request):
    """Register the user"""
    if request.method == "POST":
        user = CustomUser()
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        user.email = request.POST.get('mail')
        user.age = request.POST.get('age')
        user.address = request.POST.get('address')
        user.phone = request.POST.get('phone')
        user.password = make_password(request.POST.get('password'))
        user.username = request.POST.get('mail')
        user.save()
    return render(request,'register.html')
    
def songupload(request):
    return render(request,'songupload.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request,"You have successfully been logged out")
    return redirect(reverse('index')) 
    
def login(request):
    """Return a login page"""
    if request.method == "POST":
        login_form =UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            messages.success(request,"You've sucessfully logged in!")
        
            if user:
                 auth.login(user=user, request=request)
                 return redirect(reverse('index')) 
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request,'login.html', {'login_form': login_form})
    
def user_profile(request):
    """the users profile page"""
    user = request.user
    return render(request,'profile.html',{"profile": user})
