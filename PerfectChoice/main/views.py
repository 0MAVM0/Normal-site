from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import *
from .models import *
from Profile.models import *

def home_page(request):
    user_status = {
        'is_active': request.user.is_active,
        'is_staff': request.user.is_staff,
        'is_superuser': request.user.is_superuser,
        'username': request.user.username,
    }
    profile = UserProfile.objects.all()
    user_profile = UserProfile.objects.get(user=request.user) if request.user.is_authenticated else None

    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name

    context = {
        'user_status': user_status,
        'profiles': profile,
        'user_profile': user_profile,
        'user_group': user_group
    }

    return render(request, 'main/home.html', context)

def about(request):
    return render(request, 'main/about.html')


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f"Welcome to our site {username}!")
            form.save()
            return redirect('login')
    else:
        form = UserForm()

    context = {'form': form}
    return render(request, 'main/allAuth/registrator.html', context)
