from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

@login_required(login_url=settings.DONOR_LOGIN_URL)
def donor(request):
    return render(request, 'donor.html')