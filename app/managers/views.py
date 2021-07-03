from rest_framework.view import APIView
from rest_framework.response import Response

from .models import ManagerModel
from .serializer import ManagerSerializer

class ManagerEndPoint(APIView):

    def get(self, request):

        managers = ManagerModel.objects.all()
        managers_serializer = ManagerSerializer(managers, many=True)
        return Response(managers_serializer.data)

