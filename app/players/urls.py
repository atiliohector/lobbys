from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.AllPlayers.as_view(), name='all_players'),
    path('create/', views.CreatePlayer.as_view(), name='create_player'),
    path('update/<int:id>/', views.UpdatePlayer.as_view(), name='update_player'),
    path('delete/<int:id>/', views.DeletePlayer.as_view(), name='delete_player')

]