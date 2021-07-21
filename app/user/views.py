from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserModel
from .serializer import UserSerializer

class AllUser(APIView):
    
    def get(self, request):

        users = UserModel.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data)

class AddUser(APIView):

    def post(self, request):

        data = {

            'name':request.data.get('name'),
            'age': request.data.get('age'),
            'profession': request.data.get('profession')

        }   

        user_serializer = UserSerializer(data=data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        else:
            return Response(user_serializer.errors)

class SpecificUser(APIView):

    def get_user(self, id):

        try:
            return UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            return Response('Its was not this time!')
    
    def get(self, request, id):

        user_baby = self.get_user(id=id)
        user_serializer = UserSerializer(user_baby)
        try:
            return Response(user_serializer.data)
        except UserModel.DoesNotExist:
            return Response('Does not exist! ')


    def delelete(self, request, id):
        
        user_baby = self.get_user(id)
        user_baby.delelete()
        return Response('Deleted successfully!')
