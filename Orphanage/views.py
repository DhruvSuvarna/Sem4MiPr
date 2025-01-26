from django.shortcuts import render, redirect
from .models import Orphanage_Details, Orphanage_Events
from Orph.models import Orphanage_Display
from Donor.models import UtilityDonation, ServiceDonation, DonorProfile, Visits
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def orphanage(request):
    username = request.user.username

    if Orphanage_Details.objects.filter(username= username).exists():
        specialCheck = "hey i am defined"
        return render(request,'orphanage.html',{'specialCheck': specialCheck})
    
    return render(request,'orphanage.html')

@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def view_donations(request):
    username = request.user.username
    if UtilityDonation.objects.filter(orphanageusername= username).exists() or ServiceDonation.objects.filter(orphanageusername= username).exists():
        utilitydonations = UtilityDonation.objects.filter(orphanageusername= username)
        servicedonations = ServiceDonation.objects.filter(orphanageusername= username)
        donorprofiles = DonorProfile.objects.all()
        check = 1
        total = 0
        for u_donation in utilitydonations:
            total += u_donation.money
        if Orphanage_Details.objects.filter(username= username).exists():
            specialCheck = "hey i am defined"
            return render(request, 'o_view_donations.html', {'specialCheck': specialCheck, 'donorprofiles': donorprofiles,'utilitydonations': utilitydonations, 'total': total, 'servicedonations': servicedonations, 'check': check, 'scroll_target': '#main-content'})
        
        return render(request, 'o_view_donations.html', {'donorprofiles': donorprofiles,'utilitydonations': utilitydonations, 'total': total, 'servicedonations': servicedonations, 'check': check, 'scroll_target': '#main-content'})
   
    else:
        nodonations = "You haven't received any donations yet"
        check = 0
        if Orphanage_Details.objects.filter(username= username).exists():
            specialCheck = "hey i am defined"
            return render(request, 'o_view_donations.html', {'specialCheck': specialCheck,'nodonations': nodonations, 'check': check, 'scroll_target': '#main-content'})
        
        return render(request, 'o_view_donations.html', {'nodonations': nodonations, 'check': check, 'scroll_target': '#main-content'})

@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def add_details(request):
    username = request.user.username
    if Orphanage_Details.objects.filter(username= username).exists():
        
        specialCheck = "hey i am defined"
        orphanage = Orphanage_Details.objects.get(username= username)
        orphanage_dis = Orphanage_Display.objects.get(username= username)
        if request.method == 'POST':
            o_name = request.POST['o_name']
            o_img = request.FILES['o_img'] # Access the uploaded file using request.FILES
            o_state = request.POST['o_state']
            o_city = request.POST['o_city']
            o_district = request.POST['o_district']
            o_address = request.POST['o_address']
            o_weblink = request.POST['o_weblink']

            if o_img:
                fs = FileSystemStorage()
                filename = fs.save('pics/' + o_img.name, o_img)
            if o_name:
                orphanage.o_name = o_name
                orphanage_dis.name = o_name
            if filename:
                orphanage.o_img = filename
                orphanage_dis.img = filename
            if o_state:
                orphanage.o_state = o_state
                s = orphanage_dis.location
                words = s.split(", ") 
                words[2] = o_state 
                new_s = ", ".join(words)
                orphanage_dis.location = new_s
                orphanage_dis.save()
            if o_city:
                orphanage.o_city = o_city
                s = orphanage_dis.location
                words = s.split(", ") 
                words[1] = o_city 
                new_s = ", ".join(words)
                orphanage_dis.location = new_s
                orphanage_dis.save()
            if o_district:
                orphanage.o_district = o_district
                s = orphanage_dis.location
                words = s.split(", ") 
                words[0] = o_district 
                new_s = ", ".join(words)
                orphanage_dis.location = new_s
                orphanage_dis.save()
            if o_address:
                orphanage.o_address = o_address
            if o_weblink:
                orphanage.o_weblink = o_weblink
                orphanage_dis.weblink = o_weblink
            orphanage.save()
            orphanage_dis.save()
            success_message = 'Details Edited Successfully!'
            return render(request, 'o_add_details.html', {'specialCheck': specialCheck, 'scroll_target': '#main-content', 'orphanage': orphanage,'messages': success_message})

        return render(request, 'o_add_details.html', {'specialCheck': specialCheck, 'scroll_target': '#main-content', 'orphanage': orphanage})
        
    else:
    
        if request.method == 'POST':
            o_name = request.POST['o_name']
            o_img = request.FILES['o_img'] # Access the uploaded file using request.FILES
            o_state = request.POST['o_state']
            o_city = request.POST['o_city']
            o_district = request.POST['o_district']
            o_address = request.POST['o_address']
            o_weblink = request.POST['o_weblink']

            if request.user.is_authenticated and request.user.role=='orphanage':
                username = request.user.username

                fs = FileSystemStorage()
                filename = fs.save('pics/' + o_img.name, o_img)

                orphanage_details = Orphanage_Details.objects.create(username= username, o_name= o_name, o_img= filename, o_state= o_state, o_city= o_city, o_district= o_district, o_address= o_address, o_weblink= o_weblink)
                orphanage_details.save()
                location = o_district+', '+o_city+', '+o_state
                orphanage_display = Orphanage_Display.objects.create(username= username, name= o_name, img= filename, location= location, weblink= o_weblink)
                orphanage_display.save()
                messages.info(request, 'Details Added Successfully!')
                return redirect('add_details')

            elif request.user.is_authenticated and request.user.role=='donor':
                messages.info(request, 'Donors cannot add details!')
                # specialCheck = 0
                return redirect('add_details', {'scroll_target': '#main-content'})
            
            elif request.user.is_authenticated and request.user.role=='donor':
                messages.info(request, 'Admins cannot add details!')
                # specialCheck = 0
                return redirect('add_details', {'scroll_target': '#main-content'})
            
            else:
                messages.info(request, 'You need to Login first!')
                specialCheck = 0
                return redirect('add_details', {'scroll_target': '#main-content'})

        # specialCheck = 0   
        return render(request, 'o_add_details.html', {'scroll_target': '#main-content'})

@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def view_details(request):
    
    username = request.user.username
    if Orphanage_Details.objects.filter(username= username).exists():
        details = Orphanage_Details.objects.filter(username= username)
        check = 1
        specialCheck = "hey i am defined"
        return render(request, 'o_view_details.html', {'specialCheck': specialCheck, 'details': details, 'check': check, 'scroll_target': '#main-content'})
    
    else:
        nodetails = "You have not added any details yet"
        check = 0
        return render(request, 'o_view_details.html', {'nodetails': nodetails, 'check': check, 'scroll_target': '#main-content'})
    
@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def add_events(request):
    username = request.user.username
    if Orphanage_Details.objects.filter(username= username).exists():
        specialCheck = "hey i am defined"
        # if Orphanage_Events.objects.filter(username= username).exists():
        #     check2 = "You have already added your details"
        #     if request.method == 'POST':
        #         e_name = request.POST['e_name']
        #         e_desc = request.POST['e_desc']
        #         e_img = request.FILES['e_img']
        #         startdate = request.POST['e_sdate']
        #         enddate = request.POST['e_edate']

        #         orphanage = Orphanage_Details.objects.get(username=username)
        #         o_name = orphanage.o_name
        #         if e_img:
        #             fs = FileSystemStorage()
        #             filename = fs.save('pics/' + e_img.name, e_img)

        #         o_event = Orphanage_Events.objects.get(username= username)
        #         if e_name:
        #             o_event.e_name = e_name
        #         if e_desc:
        #             o_event.e_desc = e_desc
        #         if filename:
        #             o_event.e_img = filename
        #         if startdate:
        #             o_event.e_sdate = startdate
        #         if enddate:
        #             o_event.e_edate = enddate
        #         o_event.save()

        #         message2 = 'Event edited successfully'

        #         return render(request, 'o_add_events.html', {'check2': check2})


        #     return render(request, 'o_add_events.html', {'check2': check2})
        # else:
        if request.method == 'POST':
                e_name = request.POST['e_name']
                e_desc = request.POST['e_desc']
                e_img = request.FILES['e_img']
                startdate = request.POST['e_sdate']
                enddate = request.POST['e_edate']

                orphanage = Orphanage_Details.objects.get(username=username)
                o_name = orphanage.o_name
                fs = FileSystemStorage()
                filename = fs.save('pics/' + e_img.name, e_img)

                orphanage_event = Orphanage_Events.objects.create(username=username, o_name= o_name, e_name= e_name, e_desc=e_desc, e_img= filename, startdate= startdate, enddate = enddate)
                orphanage_event.save()
                messages.info(request, 'Event added successfully')
                return redirect('add_events')

        return render(request, 'o_add_events.html', {'specialCheck': specialCheck, 'scroll_target': '#main-content'})
        
    else:
        check = "Add your orphanage details first"
        return render(request, 'o_add_events.html', {'check': check})
    
@login_required(login_url=settings.ORPHANAGE_LOGIN_URL)
def check_visits(request):
    username = request.user.username
    if Visits.objects.filter(orphanageusername= username).exists():
        visitsAll = Visits.objects.all()
        visits = []
        i=0
        for visit in visitsAll:
            if visit.orphanageusername == username:
                visits.append(visit)
                visits[0].pic = DonorProfile.objects.get(username=visit.donorusername).profile_pic.url
                reason = visits[0].reason
                if 'your' in reason:
                    visits[0].reason = reason.replace('your', 'their')
                i += 1
        if request.method == 'POST':
            choice = request.POST['choice']
            donorname = request.POST['donorname']
            visit = Visits.objects.get(donorusername= donorname)
            visit.status = choice
            visit.save()
            for v in visits:
                if v.donorusername == donorname:
                    v.status = choice
            return render(request, 'o_check_visits.html', {'scroll_target': '#main-content', 'visits': visits})
        # donorname = visits.donorusername
        # donors = Donorprofile.objects.filter(username=donorname)
        return render(request, 'o_check_visits.html', {'scroll_target': '#main-content', 'visits': visits})
    else:
        return render(request, 'o_check_visits.html', {'scroll_target': '#main-content'})