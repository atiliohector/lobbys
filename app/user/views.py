from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserModel
from .serializer import UserSerializer

class AllUsers(APIView):

    def get(self, request):
        users = UserModel.objects.all()
        user_serializer = UserSerializer(users,many=True)
        return Response(user_serializer.data)