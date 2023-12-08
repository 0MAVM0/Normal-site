from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('about/', about, name='about'),
    path('registrate/', registration, name="signup"),
    path('login/', LoginView.as_view(template_name="main/allAuth/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name='main/allAuth/logout.html'), name='logout'),
    path('accounts/', include('allauth.urls'), name='google_login'),

    # CRUD
    path('product/', product, name='product'),
    path('product/my_product/', my_products, name='my_product'),
    path('product/create/', create_product, name='create_product'),
    path('product/<int:product_id>/', view_product, name='view_product'),
    path('product/<int:product_id>/edit', edit_product, name='edit_product'),
    path('product/<int:product_id>/delete/', delete_product, name='delete_product')
]
