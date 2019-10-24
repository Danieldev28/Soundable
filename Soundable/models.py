from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# ---------------------------------------------------custom user model----------->
class CustomUser(AbstractUser):
    address = models.CharField(max_length=300,null=True)
    age = models.IntegerField(null = True)
    phone = models.CharField(max_length = 20, null = True)
    is_active = models.BooleanField(default=True)

class mood(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return (self.name)


class genre(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return (self.name)
        
class tempo(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return (self.name)

class soundslike(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return (self.name)


class gender(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return (self.name)
    

class Type(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return (self.name)
        
class song_table(models.Model):
    name = models.CharField(max_length=50)
    lyrics = models.CharField(max_length=7000, null=True)
    time = models.IntegerField()
    downloadfile = models.FileField(upload_to='songs/')
    genre = models.ForeignKey(genre, on_delete=models.CASCADE)
    soundslike = models.ForeignKey(soundslike, on_delete=models.CASCADE)
    tempo = models.ForeignKey(tempo, on_delete=models.CASCADE)
    gender = models.ForeignKey(gender, on_delete=models.CASCADE)
    mood = models.ForeignKey(mood, on_delete=models.CASCADE)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE)
    buyer = models.ForeignKey(CustomUser, related_name="buyer_user", null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    creator = models.ForeignKey(CustomUser, related_name="creator_user", on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.name)
    
class userprofile_table(models.Model):
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return (self.user.username)

class purchases(models.Model):
    billing_address = models.CharField(max_length=500)
    song = models.ForeignKey(song_table, on_delete=models.CASCADE)
    price = models.IntegerField()
    purchased_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return (self.song.name)
        

class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    
     
    def __str__(self):
        return (self.name)

class subscriber(models.Model):
    email = models.CharField(max_length=50)
    
     
    def __str__(self):
        return (self.email)
        

    
    

   
