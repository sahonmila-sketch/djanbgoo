from django.db import models

class UserModel(models.Model):
    namege = models.CharField(max_length=100)
    emailge = models.EmailField(unique=True)
    agege = models.IntegerField()

    def __str__(self):
        return self.namege
# Create your models here.
