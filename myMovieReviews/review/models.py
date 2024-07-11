from django.db import models


# Create your models here.

class Review(models.Model):



    title = models.CharField(max_length=30)
    review = models.TextField()
    genre = models.CharField(max_length=5)
    year=models.CharField(max_length=5, default='0')
    rate = models.CharField(max_length=3, default='0')
    movie_time = models.PositiveIntegerField()
    img_url = models.ImageField(upload_to='images/', default='images/basic.jpg')
    director = models.CharField(max_length=10)
    actor = models.CharField(max_length=10)
