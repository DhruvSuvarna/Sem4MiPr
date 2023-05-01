from django.shortcuts import render
from .models import Orphanage_Display
from Donor.models import UtilityDonation, ServiceDonation
from Orphanage.models import Orphanage_Details
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    if request.method == 'POST':
        district = request.POST['search']
        district = district.title()
        print(district)
        orphs = Orphanage_Display.objects.filter(location__startswith=district)
        return render(request,'index.html', {'orphs':orphs, 'scroll_target': '#ao'} )
    
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
    if request.method == 'POST':
        form_id = request.POST['form_id']
        if form_id == "SubmitUtilityDonation":
            donorname = request.POST['donorname']
            orphanagename = request.POST['orphanagename']
            money = request.POST['money']
            grains_no = request.POST['grains_no']
            grains = request.POST['grains']
            books_no = request.POST['books_no']
            books = request.POST['books']

            orphanageusername = Orphanage_Details.objects.get(o_name = orphanagename)
            img = orphanageusername.o_img.url
            orphanageusername = orphanageusername.username

            utility_donation = UtilityDonation.objects.create(donorname = donorname, orphanageusername = orphanageusername, orphanagename = orphanagename, money = money, grains_no = grains_no , grains = grains, books_no = books_no, books = books)
            utility_donation.save()
            message = "Utility Donated"
            return render(request,'donate.html', {'message' : message, 'utdonation':utility_donation, 'img': img})

        elif form_id == "SubmitServiceDonation":
            donorname = request.POST['donorname2']
            orphanagename = request.POST['orphanagename2']
            service = request.POST['service2']
            mobile = request.POST['mobile2']

            orphanageusername = Orphanage_Details.objects.get(o_name = orphanagename)
            img = orphanageusername.o_img.url
            orphanageusername = orphanageusername.username

            service_donation = ServiceDonation.objects.create(donorname = donorname, orphanageusername = orphanageusername, orphanagename = orphanagename, service = service, mobile = mobile)
            service_donation.save()
            message = "Service Donated"
            return render(request,'donate.html', {'message' : message, 'svdonation':service_donation, 'img': img})

    orphs = Orphanage_Display.objects.all()
    return render(request,'donate.html', {'orphs': orphs})
    