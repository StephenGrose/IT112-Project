from django.shortcuts import render, get_object_or_404
from .models import ffGame, ffReview
from .forms import GameForm, ReviewForm
from django.contrib.auth.decorators import login_required

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

def gamereviews(request, game_id):
    gamereviews=ffReview.objects.filter(game=game_id)
    return render(request, 'ffreviews/gamereviews.html', {'gamereviews': gamereviews})

@login_required
def newGame(request):
    form=GameForm

    if request.method=='POST':
        form=GameForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=GameForm()
    else:
        form=GameForm()
    return render(request, 'ffreviews/newgame.html', {'form': form})

@login_required
def newReview(request):
    form=ReviewForm

    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'ffreviews/newreview.html', {'form': form})

def logoutmessage(request):
    return render(request, 'ffreviews/logoutmessage.html')

def loginmessage(request):
    return render(request, 'ffreviews/loginmessage.html')