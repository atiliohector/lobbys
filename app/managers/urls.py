from django.urls import path

from . import views

urlpatterns = [

    path('', views.ManagerEndPoint.as_view(), name='all_managers'),

]