from django.http.response import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PlayerModel
from .serializer import PlayerSerializer


class PlayersEndPoint(APIView):

    def get(self, request):

        players = PlayerModel.objects.all()
        player_serializer = PlayerSerializer(players, many=True)
        return Response(player_serializer.data)

    def post(self, request):

        data = {

            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'position': request.data.get('position'),
            'guild': request.data.get('guild'),

        } 

        player = PlayerSerializer(data=data)

        if player.is_valid():
            player.save()
            return Response(player.data)
        else:
            return Response(player.errors)

class JustPlayer(APIView):

    def get_player(self, id):
        try:
            return PlayerModel.objects.get(id=id)
        except PlayerModel.DoesNotExist:
            return Http404
    
    def get(self, request, id):

        player = self.get_player(id=id)
        player_serializer = PlayerSerializer(player)
        return Response(player_serializer.data)

    def delete(self, request, id):

        player = self.get_player(id=id)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):

        player = self.get_player(id)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class PlayerByPosition(APIView):

    def get(self, request, position):

        player = PlayerModel.objects.filter(position=position)
        player_serializer = PlayerSerializer(player, many=True)
        return Response(player_serializer.data)