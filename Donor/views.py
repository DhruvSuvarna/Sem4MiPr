from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import DonorProfile, Visits
from Orph.models import Orphanage_Display
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.

@login_required(login_url=settings.DONOR_LOGIN_URL)
def donor(request):
    username = request.user.username
    donor=''
    if DonorProfile.objects.filter(username= username).exists:
        donors = DonorProfile.objects.all()
        for d in donors:
            if d.username == username:
                donor = d
        return render(request, 'donor.html', {'donor': donor})
    else:
        return render(request, 'donor.html')

@login_required(login_url=settings.DONOR_LOGIN_URL)
def add_profile(request):
    username = request.user.username
    if DonorProfile.objects.filter(username= username).exists():
        
        specialCheck = "hey i am defined"
        username = request.user.username
        profile_pic = ''
        donor = DonorProfile.objects.get(username= username)
        return render(request, 'd_add_profile.html', {'specialCheck': specialCheck, 'scroll_target': 'main-content', 'donor': donor})
        
    else:
    
        if request.method == 'POST':
            profile_pic = request.FILES['profile_pic'] # Access the uploaded file using request.FILES
            mobile = request.POST['mobile']
            location = request.POST['location']

            if request.user.is_authenticated and request.user.role=='donor':
                username = request.user.username
                donors = CustomUser.objects.all()
                name = ''
                for donor in donors:
                    if donor.username == username:
                        name = donor.first_name + ' ' + donor.last_name
                fs = FileSystemStorage()
                filename = fs.save('pics/' + profile_pic.name, profile_pic)

                profile = DonorProfile.objects.create(username = username, name = name, profile_pic= filename, mobile= mobile, location= location)
                profile.save()
                messages.info(request, 'Details Added Successfully!')
                return redirect('add_profile')

            elif request.user.is_authenticated and request.user.role=='orphanage':
                messages.info(request, 'Orphanages cannot add details!')
                return redirect('add_profile', {'scroll_target': 'main-content'})
            
            elif request.user.is_authenticated and request.user.role=='donor':
                messages.info(request, 'Admins cannot add details!')
                return redirect('add_profile', {'scroll_target': 'main-content'})
            
            else:
                messages.info(request, 'You need to Login first!')
                return redirect('add_profile', {'scroll_target': 'main-content'})

    return render(request, 'd_add_profile.html', {'scroll_target': 'main-content'})

def visit(request):
    username = request.user.username
    if DonorProfile.objects.filter(username= username).exists:
        donor = DonorProfile.objects.get(username= username)

        orphs = Orphanage_Display.objects.all()

        if request.method == 'POST':
            reason = request.POST['reason']
            orphanagename = request.POST['orphanage']
            date = request.POST['date']

            orph = Orphanage_Display.objects.get(name= orphanagename)
            orphanageusername = orph.username

            mobile = donor.mobile            
            donorusername = donor.username  

            visit = Visits.objects.create(donorusername= donorusername, orphanageusername= orphanageusername, orphanagename= orphanagename, reason= reason, mobile= mobile, date=date)
            visit.save()
            messages.info(request, 'Application sent successfully!')
            return render(request, 'visit.html', {'scroll_target': 'main-content', 'donor': donor, 'orphs': orphs})

        return render(request, 'visit.html', {'scroll_target': 'main-content', 'donor': donor, 'orphs': orphs})
        
    else: 
        reminder = "You have to complete your profile first"
        return render(request, 'visit.html', {'scroll_target': 'main-content', 'reminder': reminder})