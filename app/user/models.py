from django.db import models

class UserModel(models.Model):

    name = models.CharField(max_length=255)
    age = models.IntegerField(default=18)
    type_user = models.CharField(max_length=255)
    mode_game = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name    