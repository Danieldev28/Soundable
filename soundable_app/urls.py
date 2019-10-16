"""soundable_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Soundable.views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , index, name='index'),
    url(r'^contact/$', contact_us, name='contact'),
    url(r'^artists/$', artists, name='artists'),
    url(r'^artist/$', artist, name= 'artist'),
    url(r'^blog.html/$', blog, name= 'blog'),
    # url(r'^login.html/$', login, name= 'login'),
    url(r'^register.html/$', register, name= 'register'),
    url(r'^songupload.html/$', songupload, name= 'songupload'),
    url(r'^accounts/logout/$', logout, name= 'logout'),
    url(r'^accounts/login/$', login, name= 'login'),
    
    
    


    
]
