from django.db import models

class UserModel(models.Model):

    name = models.CharField('Name', max_length=255, blank=False)
    age = models.IntegerField('Age', default=18, blank=False)
    profession = models.CharField('Profession', max_length=255, blank=True, null=True)
    

    def __str__(self):
        return self.name
