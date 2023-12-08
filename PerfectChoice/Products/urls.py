from django.urls import path

from .views import *


urlpatterns = [
    path('', product, name='product'),
    path('my_product/', my_products, name='my_product'),
    path('create/', create_product, name='create_product'),
    path('<int:product_id>/', view_product, name='view_product'),
    path('<int:product_id>/edit', edit_product, name='edit_product'),
    path('<int:product_id>/delete/', delete_product, name='delete_product')
]
