import django_filters
from blog.models import Stori

class StoriFilter(django_filters.FilterSet):
     
   
     class Meta:
         model = Stori
         fields = {
            'title': ['icontains'],
            'created_at':['lt', 'gt']
          }