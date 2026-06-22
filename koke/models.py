from django.db import models

class UserModel(models.Model):
    name3 = models.CharField(max_length=255)
    surname3 = models.CharField(max_length=255)
    username3 = models.CharField(max_length=150, unique=True)
    email3 = models.EmailField(unique=True)
    password3 = models.CharField(max_length=128)
    def __str__(self):
        return self.username3

# Create your models here.
