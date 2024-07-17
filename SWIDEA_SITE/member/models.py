from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=24)
    age = models.IntegerField(default=0)
