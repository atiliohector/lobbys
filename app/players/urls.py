from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.AllPlayers.as_view(), name='all_players'),

]