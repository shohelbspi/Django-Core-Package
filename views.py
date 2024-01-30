from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'core/base.html')

def login(request):
    return render(request,'core/login.html')