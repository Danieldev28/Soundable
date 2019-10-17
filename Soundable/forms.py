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
    """Form used to register a new user"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_datat.get('username')
        if User.objects.filter(email=email).exclude(username=username):
                raise forms.ValidationError('Your email address must be unique, try another email')
        return email
  
    
class UserContactForm(forms.Form):
    
    class Meta: 
        model= contact
        fields:('name', 'email', 'subject', 'message')

class Usersubscriber(forms.Form):
    
    class Meta:
        model= subscriber
        fields:('email')
    