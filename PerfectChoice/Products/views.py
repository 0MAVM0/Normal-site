from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, redirect

from .forms import *
from .models import *
from Profile.models import *


def product(request):
    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name
    products = Product.objects.all()

    user_status = {
        'username': request.user.username,
    }

    context = {
        'products': products,
        'user_status': user_status,
        'user_group': user_group
    }

    return render(request, 'products/product.html', context)

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    profile = UserProfile.objects.all()
    user_status = {
        'username': request.user.username,
    }
    if request.user != product.user and not request.user.is_superuser and request.user.groups.first().name != 'Admin':
        return redirect('product')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
        'user_status': user_status
    }

    return render(request, 'products/edit_product.html', context)

def view_product(request, product_id):
    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name
    product = get_object_or_404(Product, id=product_id)

    creator_profile = UserProfile.objects.get(user=product.user)

    context = {
        'product': product,
        'user_status': {
            'username': request.user.username
        },
        'creator_profile': creator_profile,
        'user_group': user_group
    }

    return render(request, 'products/view_product.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user == product.user or request.user.is_superuser:
        product.delete()
    return redirect('product')

def create_product(request):
    profile = UserProfile.objects.all()
    user_status = {
        'username': request.user.username,
    }
    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('product') 
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'user_group': user_group,
        'user_status': user_status
    }

    return render(request, 'products/create_product.html', context)

def my_products(request):
    user_status = {
        'username': request.user.username,
    }
    user_group = None
    if request.user.groups.exists():
        user_group = request.user.groups.first().name
        
    if request.user.is_authenticated:
        user_products = Product.objects.filter(user=request.user)

        context = {
            'user_products': user_products,
            'user_group': user_group,
            'user_status': user_status
        }

        return render(request, 'products/my_products.html', context)
    else:
        context = {
            'user_products': [],
            'user_group': user_group,
            'user_status': user_status
        }

        return render(request, 'products/my_products.html', context)
