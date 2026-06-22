from django.db import models

class UserModel(models.Model):
    name4 = models.CharField(max_length=255)
    surname4 = models.CharField(max_length=255)
    username4 = models.CharField(max_length=150, unique=True)
    email4 = models.EmailField(unique=True)
    password4 = models.CharField(max_length=128)
    def __str__(self):
        return self.username4

# Create your models here.
