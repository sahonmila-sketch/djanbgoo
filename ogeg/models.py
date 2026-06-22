from django.db import models

class UserModel(models.Model):
    nameeg = models.CharField(max_length=100)
    emaileg = models.EmailField(unique=True)
    ageeg = models.IntegerField()
    def __str__(self):
        return self.nameeg

# Create your models here.
