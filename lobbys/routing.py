from django.urls import path

from .consumers import WSConsumer

websocketpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi())
]