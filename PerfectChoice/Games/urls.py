from django.urls import path

from .views import *


urlpatterns = [
    path('', games, name='games'),
    path('tetris/', tetris, name='tetris'),
]
