from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from .views import *


urlpatterns = [
    path('', home_page, name='home_page'),
    path('registrate/', registration, name="signup"),
    path('login/', LoginView.as_view(template_name="main/allAuth/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name='main/allAuth/logout.html'), name='logout'),
    path('accounts/', include('allauth.urls'), name='google_login'),
]
