from rest_framework import serializers

from .models import PlayerModel, GuildModels

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerModel
        fields = (
            "id",
            "name",
            "age",
            "type_user",
            "mode_game",
        )

class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuildModels
        fields = '__all__'
