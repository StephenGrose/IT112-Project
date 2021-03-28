from django.shortcuts import render, get_object_or_404
from .models import ffGame, ffReview

# Create your views here.
def index (request):
    		return render(request, 'ffreviews/index.html')

def getgames(request):
	game_list=ffGame.objects.all()
	return render(request,'ffreviews/games.html',{'game_list': game_list})

def gamedetails(request, id):
	game=get_object_or_404(ffGame,pk=id)
	releasedate=game.gameReleaseDate
	platform=game.gameReleasePlatform
	summary=game.gameSummary
	context={
		'game' : game,
		'releasedate' : releasedate,
		'platform' : platform,
		'summary' : summary,
	}
	return render(request, 'ffreviews/gamedetails.html',context=context)
