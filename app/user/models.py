from django.db import models

class UserModel(models.Model):

    name = models.CharField(max_length)