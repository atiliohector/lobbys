from rest_framework import serializers

from .models import ManagerModel

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerModel
        fields = '__all__'