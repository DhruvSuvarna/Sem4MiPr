from django.shortcuts import render
from .models import Orphanage_Display
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):

    orphs = Orphanage_Display.objects.all()
    return render(request,'index.html', {'orphs':orphs})

@login_required(login_url=settings.DONOR_LOGIN_URL)
def about(request):

    return render(request,'about.html')

@login_required(login_url=settings.DONOR_LOGIN_URL)
def suggestion(request):

    return render(request,'suggestion.html')

@login_required(login_url=settings.DONOR_LOGIN_URL)
def donation(request):

    return render(request,'donate.html')

