from django.shortcuts import render

# Create your views here.

def orphanage(request):

    return render(request,'orphanage.html')

def view_donations(request):
    donations = [ 'donation 1', 'donation 2', 'donation 3']
    return render(request, 'o_view_donations.html', {'donations': donations})

def add_details(request):
    if request.method == 'POST':
        o_name = request.POST['o_name']
        if request.FILES == 'o_img':
            o_img = request.FILES['o_img']
    return render(request, 'o_add_details.html')


def view_details(request):
    details = [ 'detail 1', 'detail 2', 'detail 3']
    return render(request, 'o_view_details.html', {'details': details})