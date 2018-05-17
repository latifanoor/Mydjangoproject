from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def swahilipot(request):
    return render(request,'swahilipot/latifa.html')