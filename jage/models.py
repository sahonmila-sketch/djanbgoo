from django.db import models

class UserModel(models.Model):
    nameja = models.CharField(max_length=100)
    emailja = models.EmailField(unique=True)
    ageja = models.IntegerField()
    def __str__(self):
        return self.nameja

# Create your models here.
