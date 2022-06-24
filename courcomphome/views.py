from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'courcomp/index.html')

def courselist(request):
    return render(request,'courcomp/courselist.html')



