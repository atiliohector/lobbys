from django.urls import path

from . import views

urlpatterns = [

    path('all/', views.AllUser.as_view()),
    path('add/', views.AddUser.as_view()),
    path('<int:id>/', views.SpecificUser.as_view()),
]