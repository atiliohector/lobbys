from django.db import models

class UserModel(models.Model):

    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    type_user = models.CharField(max_length=50)
    mode_game = models.CharField(max_length=50, blank=True, null=True, default=None)
    guild = models.CharField(max_length=50, blank=True, null=True, default=None)


    def __str__(self):
        return self.name
