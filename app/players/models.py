from django.db import models

#Adicionar celular ou computador

class PlayerModel(models.Model):
    name = models.CharField('Name', max_length=255, blank=False)
    age = models.PositiveIntegerField('Age', blank=False, default=18)
    position = models.CharField('Position', blank=False, max_length=255)
    guild = models.CharField('Guild', blank=False, max_length=255)
    

    def __str__(self):
        return self.name