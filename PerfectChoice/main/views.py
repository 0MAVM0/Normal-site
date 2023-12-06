from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import Profile


def home_page(request):
    return render(request, 'main/home.html')

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

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'main/profile.html', context)
