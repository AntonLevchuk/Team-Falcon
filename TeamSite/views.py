from django.shortcuts import render
from .models import Players, Tournaments
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'TeamFalcon',
    }
    return render(request, 'TeamSite/index.html', context)


def tournaments(request):
    context = {
        'title': 'Турниры'
    }
    return render(request, 'TeamSite/tournaments.html', context)


def players(request):
    player = Players.objects.order_by('-created_at')
    context = {
        'player': player,
        'title': 'TeamFalcon',
    }
    return render(request, 'TeamSite/players.html', context)
