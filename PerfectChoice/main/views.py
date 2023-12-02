from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def home_page(request):
    return render(request, 'main/home.html')


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_profile = form.save(commit=False)
            user_profile.user = user
            user_profile.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'main/allAuth/registrator.html', context)