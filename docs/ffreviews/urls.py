from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('getgames/',views.getgames,name='games'),
    path('gamedetails/<int:id>',views.gamedetails, name='gamedetails'),
    path('gamereviews/<int:game_id>', views.gamereviews, name='gamereviews'),
    path('newgame/', views.newGame, name='newgame'),
    path('newreview/', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]