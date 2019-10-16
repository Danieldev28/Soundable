from django import forms
from Soundable.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model= CustomUser
        fields= ('username', 'email',)
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model= CustomUser
        fields=('username', 'email')
        
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserContactForm(forms.Form):
    
    class Meta: 
        model= contact
        fields:('name', 'email', 'subject', 'message')

class Usersubscriber(forms.Form):
    
    class Meta:
        model= subscriber
        fields:('email')
    