from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import CustomUser
from django.contrib import messages

# Create your views here.

# Donor authentication below

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            else:
                customuser = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1, role='donor')
                customuser.save()
                print('customuser created')
                return redirect('signin')

        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        customuser = auth.authenticate(username=username, password=password)
        U = CustomUser.objects.get(username=username)

        if U.role == 'donor':
            if customuser is not None:
                auth.login(request, customuser)
                return redirect('/')
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('signin')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('signin')

    else:
        return render(request, "signin.html")


def signout(request):
    auth.logout(request)
    return redirect('/')


# Orphanage authentication below

def o_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('o_signup')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('o_signup')
            else:
                customuser = CustomUser.objects.create_user(username=username, email=email, password=password1, role='orphanage')
                customuser.save()
                print('customuser created')
                return redirect('o_signin')

        else:
            messages.info(request, 'Password not matching')
            return redirect('o_signup')

    else:
        return render(request, 'o_signup.html')


def o_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        customuser = auth.authenticate(username=username, password=password)
        U = CustomUser.objects.get(username=username)

        if U.role == 'orphanage':
            if customuser is not None:
                auth.login(request, customuser)
                return redirect('/orphanage/')
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('o_signin')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('o_signin')

    else:
        return render(request, "o_signin.html")


def o_signout(request):
    auth.logout(request)
    return redirect('o_signin')