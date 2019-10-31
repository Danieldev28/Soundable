from Soundable.models import *
import django_filters
# Filter results of search menu.
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = song_table
        fields = ['genre__name', 'soundslike__name',  'mood__name','Type__name','gender__name','tempo__name']
        

