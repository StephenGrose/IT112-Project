from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('getgames/',views.getgames,name='games'),
    path('gamedetails/<int:id>',views.gamedetails, name='gamedetails'),
]