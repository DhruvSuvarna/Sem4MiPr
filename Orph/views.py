from django.shortcuts import render
from .models import Display_Orphanages

# Create your views here.

def home(request):

    orphs = Display_Orphanages.objects.all()
    return render(request,'index.html', {'orphs':orphs})