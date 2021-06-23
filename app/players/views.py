from django.db.models import query
from rest_framework import generics

from .models import PlayerModel
from .serializer import PlayerSerializer

class AllPlayers(generics.ListAPIView):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerSerializer

class CreatePlayer(generics.CreateAPIView):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerSerializer

class UpdatePlayer(generics.UpdateAPIView):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerSerializer

class DeletePlayer(generics.DestroyAPIView):
    queryset = PlayerModel.objects.all()
    serializer_class = PlayerSerializer