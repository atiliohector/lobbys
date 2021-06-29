from django.db import models

class ManagerModel(models.Model):
    name = models.CharField('Name', max_length=255, blank=False)
    age = models.PositiveIntegerField('Age', default=18, blank=False)
    champion_name = models.CharField('Champion Name',max_length=255, default="", blank=False)
    
    def __str__(self):
        return self.name