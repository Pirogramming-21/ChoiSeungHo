from django.db import models


# Create your models here.

class Develop(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=30)
    content = models.TextField()
