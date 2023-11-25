from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('register-or-login/', register_or_login, name='register_or_login'),
    path('logout/', LogoutView.as_view(template_name='main/allAuth/logout.html'), name='logout'),
]
