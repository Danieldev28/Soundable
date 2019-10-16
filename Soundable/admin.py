from django.contrib import admin
from Soundable.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from Soundable.forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
admin.site.register(song_table)
admin.site.register(userprofile_table)
admin.site.register(purchases)
admin.site.register(mood)
admin.site.register(genre)
admin.site.register(tempo)
admin.site.register(soundslike)
admin.site.register(gender)
admin.site.register(Type)
admin.site.register(contact)
admin.site.register(subscriber)



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser,CustomUserAdmin)