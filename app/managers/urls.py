from django.urls import path

from . import views

urlpatterns = [

    path('', views.AllManagers.as_view(), name='all_managers'),
    path('create/', views.CreateManager.as_view(), name='create_manager'),
    path('update/<int:id>/', views.UpdateManager.as_view(), name='update_manager'),
    path('delete/<int:id>/', views.DeleteManager.as_view(), name='delete_manager'),

]