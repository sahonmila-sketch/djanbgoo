from django.db import models

class UserModel(models.Model):
    name2 = models.CharField(max_length=255)
    surname2 = models.CharField(max_length=255)
    username2 = models.CharField(max_length=150, unique=True)
    email2 = models.EmailField(unique=True)
    password2 = models.CharField(max_length=128)

    def __str__(self):
        return self.username2

# Create your models here.
