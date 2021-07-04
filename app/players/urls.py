from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.PlayersEndPoint.as_view(), name='all_players'),
    path('positions/<str:position>/', views.PlayerByPosition.as_view()),
    path('one/<int:id>/', views.JustPlayer.as_view())

]