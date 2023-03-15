from django.shortcuts import render

# Create your views here.

def andhra(request):
    return render(request,'andhra.html')

def pradesh(request):
    return render(request,'pradesh.html')