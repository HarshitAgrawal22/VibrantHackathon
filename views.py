from django.contrib.auth.models import User
from django.shortcuts import render,redirect

def base(request):
    return render(request,"base.html")