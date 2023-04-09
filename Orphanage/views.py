from django.shortcuts import render, redirect
from .models import Orphanage_Details
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def orphanage(request):
    return render(request,'orphanage.html')

@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def view_donations(request):
    donations = [ 'donation 1', 'donation 2', 'donation 3']
    return render(request, 'o_view_donations.html', {'donations': donations})

@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def add_details(request):
    if request.method == 'POST':
        o_name = request.POST['o_name']
        o_img = request.POST['o_img']
        o_state = request.POST['o_name']
        o_city = request.POST['o_name']
        o_district = request.POST['o_name']
        o_address = request.POST['o_name']
        o_weblink = request.POST['o_name']

        if request.user.is_authenticated and request.user.role=='orphanage':
            username = request.user.username

            orphanage_details = Orphanage_Details.objects.create(username= username, o_name= o_name, o_img= o_img, o_state= o_state, o_city= o_city, o_district= o_district, o_address= o_address, o_weblink= o_weblink)
            orphanage_details.save()
            messages.info(request, 'Details Added Successfully!')
            return redirect('add_details')

        elif request.user.is_authenticated and request.user.role=='donor':
            messages.info(request, 'Donors cannot add details!')
            return redirect('add_details')
        
        elif request.user.is_authenticated and request.user.role=='donor':
            messages.info(request, 'Admins cannot add details!')
            return redirect('add_details')
        
        else:
            messages.info(request, 'You need to Login first!')
            return redirect('add_details')

    return render(request, 'o_add_details.html')

@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def view_details(request):
    
    username = request.user.username
    if Orphanage_Details.objects.filter(username= username).exists():
        details = Orphanage_Details.objects.filter(username= username)
        check = 1
        return render(request, 'o_view_details.html', {'details': details, 'check': check})
    
    else:
        nodetails = "You have not added any details yet"
        check = 0
        return render(request, 'o_view_details.html', {'nodetails': nodetails, 'check': check})