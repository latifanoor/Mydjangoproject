from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board


def home(request):
    boards_names = Board.objects.all()
    print(boards_names)
    return render(request, 'swahilipot/list.html', {'boards_names':boards_names})


def swahilipot(request):
    return render(request,'swahilipot/latifa.html')