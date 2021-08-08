from rest_framework import serializers

from .models import UserModel

class UserSerializer(serializers.Serializer):
    class Meta:
        model = UserModel
        fields = (
            "id",
            "age",
            "type_user",
            "mode_game",
        )