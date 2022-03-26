from django.db import models
from django.contrib.auth import AbstractUSer

class User(AbstractUser):
    pass


class Lead(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  age = models.IntegerField(default=0)
  agent = models.ForeignKey('Agent', on_delete=models.CASCADE, null=True, blank=True)


class Agent(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)