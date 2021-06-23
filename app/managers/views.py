from rest_framework import generics

from .models import ManagerModel
from .serializer import ManagerSerializer

class AllManagers(generics.ListAPIView):
    queryset = ManagerModel.objects.all()
    serializer_class = ManagerSerializer

class CreateManager(generics.CreateAPIView):
    queryset = ManagerModel.objects.all()
    serializer_class = ManagerSerializer

class UpdateManager(generics.UpdateAPIView):
    queryset = ManagerModel.objects.all()
    serializer_class = ManagerSerializer

class DeleteManager(generics.DestroyAPIView):
    queryset = ManagerModel.objects.all()
    serializer_class = ManagerSerializer