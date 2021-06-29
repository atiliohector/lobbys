from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', include('app.players.urls')),
    path('managers/', include('app.managers.urls')),
]
