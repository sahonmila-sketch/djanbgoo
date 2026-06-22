from django.db import models

class UserModel(models.Model):
    nameho = models.CharField(max_length=100)
    emailho = models.EmailField(unique=True)
    ageho = models.IntegerField()
    def __str__(self):
        return self.nameho
# Create your models here.
