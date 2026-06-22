from django.db import models

class UserModel(models.Model):
    name5 = models.CharField(max_length=255)
    surname5 = models.CharField(max_length=255)
    username5 = models.CharField(max_length=150, unique=True)
    email5 = models.EmailField(unique=True)
    password5 = models.CharField(max_length=128)
    def __str__(self):
        return self.username5
# Create your models here.
