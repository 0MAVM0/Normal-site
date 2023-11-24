from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', LoginView.as_view(template_name='main/allAuth/login.html'), name='login'),
]
