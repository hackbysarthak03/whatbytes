from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/sign-in/')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='/sign-in/')
def profile(request):
    return render(request, 'profile/profile.html')
