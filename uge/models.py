from django.db import models


class UserModel(models.Model):
    nameug = models.CharField(max_length=100)
    emailug = models.EmailField(unique=True)
    ageug = models.IntegerField()
    def __str__(self):
        return self.nameug

# Create your models here.
