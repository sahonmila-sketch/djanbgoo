from django.db import models

class UserModel(models.Model):
    namee = models.CharField(max_length=100)
    emailne = models.EmailField(unique=True)
    agene = models.IntegerField()

    def __str__(self):
        return self.namee

# Create your models here.
