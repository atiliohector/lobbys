from django.urls import path

from . import views

urlpatterns = [

    path('', views.AllManagers.as_view(), name='all_managers'),

]