from django.db import models

class PlayerModel(models.Model):

    MOBILE = "Mobile"
    COMPUTER = "Computer"

    TYPE_USER_MODE = [
        (MOBILE, "Mobile"),
        (COMPUTER, "Computer"),
    ]

    name = models.CharField('Name', max_length=50)
    age = models.IntegerField('Age', default=18)
    type_user = models.CharField('Type User', max_length=50)
    mode_game = models.CharField('Mode Game', choices=TYPE_USER_MODE, max_length=50, default=MOBILE)

    def __str__(self):
        return self.name

class GuildModels(models.Model):

    name = models.CharField('Name', max_length=255)
    size_players = models.IntegerField('Size Players', default=1)
    guild_player = models.ForeignKey(PlayerModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
