from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Register
# Create your views here.
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password or username is incorrect')
            return render(request,'login')
    
    return render(request, 'ecomapp/login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username or not email or not password or not password2:
            messages.error(request, 'All fields are required.')
            return render(request, 'ecomapp/register.html')


        if password != password2:
            messages.error(request, 'Passwords must match.')
            return render(request, 'ecomapp/register.html')

        user = Register(username=username,email=email,password=password,password2=password2)
        user.save()
        return redirect('home')
        
    return render(request, 'ecomapp/register.html')

def user_home(request):

    return render(request, 'ecomapp/home.html')