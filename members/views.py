from django.shortcuts import render

# Create your views here.
from .models import Members

def members(request):
    members_names = Members.objects.all()
    print(members_names)
    return render(request, 'members/my.html', {'members_names':members_names})