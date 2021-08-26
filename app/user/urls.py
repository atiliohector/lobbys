from django.urls import path

from . import views

urlpatterns = [

    path('all/', views.AllUsers.as_view(), name='all'),
    path('add/', views.AddUser.as_view(), name='add')
    
]