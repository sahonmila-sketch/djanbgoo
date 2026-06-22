from django.db import models

class UserModel(models.Model):
    nameme = models.CharField(max_length=100)
    emailme = models.EmailField(unique=True)
    ageme = models.IntegerField()

    def __str__(self):
        return self.nameme

# Create your models here.
