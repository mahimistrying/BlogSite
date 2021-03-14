from django.shortcuts import render
from .models import Game
# Create your views here.
def allgames(request):
    games=Game.objects
    return render(request,"games/allgames.html",{'games':games})