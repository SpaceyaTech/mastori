from django.shortcuts import render
from .models import Account

def home(request):
    return render(request,"index.html")