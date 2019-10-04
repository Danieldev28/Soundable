from django import forms
from Soundable.models import CustomUser
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
        
        