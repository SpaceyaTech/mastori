from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello SpaceyaTech</h1>')
