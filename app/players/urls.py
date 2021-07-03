from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.PlayersEndPoint.as_view(), name='all_players'),

]