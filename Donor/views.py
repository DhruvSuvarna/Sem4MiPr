from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from .models import DonorProfile
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.

@login_required(login_url=settings.DONOR_LOGIN_URL)
def donor(request):
    username = request.user.username
    profile_pic = ''
    if DonorProfile.objects.filter(username= username).exists:
        donors = DonorProfile.objects.all()
        for donor in donors:
            if donor.username == username:
                profile_pic = donor.profile_pic.url
    return render(request, 'donor.html', {'profilepic': profile_pic})

@login_required(login_url=settings.DONOR_LOGIN_URL)
def add_profile(request):
    username = request.user.username
    if DonorProfile.objects.filter(username= username).exists():
        
        specialCheck = "hey i am defined"
        username = request.user.username
        profile_pic = ''
        if DonorProfile.objects.filter(username= username).exists:
            donors = DonorProfile.objects.all()
            for donor in donors:
                if donor.username == username:
                    profile_pic = donor.profile_pic.url
        return render(request, 'd_add_profile.html', {'specialCheck': specialCheck, 'scroll_target': 'main-content', 'profilepic': profile_pic})
        
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

