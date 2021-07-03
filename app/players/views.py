from rest_framework.view import APIView
from rest_framework.response import Response

from .models import PlayerModel
from .serializer import PlayerSerializer


class PlayersEndPoint(APIView):

    def get_player(self, request):

        players = PlayerModel.objects.all()
        player_serializer = PlayerSerializer(players, many=True)
        return Response(player_serializer.data)

     