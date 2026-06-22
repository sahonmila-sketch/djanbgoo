from django.db import models

class UserModel(models.Model):
    nameke = models.CharField(max_length=100)
    emailke = models.EmailField(unique=True)
    ageke = models.IntegerField()

    def __str__(self):
        return self.nameke

# Create your models here.
