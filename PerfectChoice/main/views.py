from django.shortcuts import render

from .forms import *
from .models import *


def home_page(request):
    return render(request, 'main/home.html')


def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            context = {'user': request.user}
            return render(request, 'main/home.html', context)
        else:
            context = {'form': form}
            return render(request, 'main/allAuth/registrator.html', context)

    context = {'form': UserForm()}
    return render(request, 'main/allAuth/registrator.html', context)
