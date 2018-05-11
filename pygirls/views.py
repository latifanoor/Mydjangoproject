from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pygirls(request):
    return render(request, 'pygirls/ziri.html')
