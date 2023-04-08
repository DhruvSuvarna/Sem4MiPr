from django.shortcuts import render
from .models import Orphanage_Details
# Create your views here.

def orphanage(request):

    return render(request,'orphanage.html')

def view_donations(request):
    donations = [ 'donation 1', 'donation 2', 'donation 3']
    return render(request, 'o_view_donations.html', {'donations': donations})

def add_details(request):
    if request.method == 'POST':
        o_name = request.POST['o_name']
        o_img = request.POST['o_img']
        o_state = request.POST['o_name']
        o_city = request.POST['o_name']
        o_district = request.POST['o_name']
        o_address = request.POST['o_name']
        o_weblink = request.POST['o_name']

        orphanage_details = Orphanage_Details.objects.create(o_name= o_name, o_img= o_img, o_state= o_state, o_city= o_city, o_district= o_district, o_address= o_address, o_weblink= o_weblink)
        orphanage_details.save()
    return render(request, 'o_add_details.html')


def view_details(request):
    details = [ 'detail 1', 'detail 2', 'detail 3']
    return render(request, 'o_view_details.html', {'details': details})