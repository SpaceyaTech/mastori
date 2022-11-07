from django.http import HttpResponse
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>SpaceyaTech Blog CMS</h1>')