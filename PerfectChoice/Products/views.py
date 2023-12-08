from django.shortcuts import render, redirect, get_object_or_404, redirect

from .forms import *
from .models import *


def product(request):
    products = Product.objects.all()
    user_status = {
        'is_active': request.user.is_active,
        'is_staff': request.user.is_staff,
        'is_superuser': request.user.is_superuser,
        'username': request.user.username,
    }
    return render(request, 'products/product.html', {'products': products, 'user_status': user_status})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user != product.user and not request.user.is_superuser:
        return redirect('product')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})

def view_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/view_product.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user == product.user or request.user.is_superuser:
        product.delete()

    return redirect('product') 

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('product')
    else:
        form = ProductForm()

    return render(request, 'products/create_product.html', {'form': form})

def my_products(request):
    if request.user.is_authenticated:
        user_products = Product.objects.filter(user=request.user)
        return render(request, 'products/my_products.html', {'user_products': user_products})
    else:
        return render(request, 'products/my_products.html', {'user_products': []})