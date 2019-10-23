from Soundable.models import *
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = song_table
        fields = ['username', 'first_name', 'last_name', ]