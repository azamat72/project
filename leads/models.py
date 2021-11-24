from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Lead(models.Model):
    familiyasi = models.CharField(max_length=20)
    ismi = models.CharField(max_length=20)
    yoshi = models.IntegerField()
    full = models.TextField()
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return self.familiyasi




