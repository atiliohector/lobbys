from app import players
from rest_framework.view import APIView
from rest_framework.response import Response

from .models import PlayerModel
from .serializer import PlayerSerializer


class PlayersEndPoint(APIView):

    def get_player(self, request):

        players = PlayerModel.objects.all()
        player_serializer = PlayerSerializer(players, many=True)
        return Response(player_serializer.data)

    def post_player(self, request):

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