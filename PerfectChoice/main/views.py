from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, SignInForm


def home_page(request):
    return render(request, 'main/home.html')


def register_or_login(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        elif 'login' in request.POST:
            form = SignInForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'main/allAuth/auth.html', {'form': form})