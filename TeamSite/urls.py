from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('tournaments', tournaments, name='tournaments'),
    path('players', players, name='players'),
]