from django.urls import path

from . import api

urlpatterns = [

    path('all/', api.AllUsers.as_view(), name='all'),
    path('add/', api.AddUser.as_view(), name='add'),
    path('<int:id>/', api.SpecificUser.as_view(), name='specific')
    
]