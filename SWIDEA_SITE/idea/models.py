from django.db import models

from develop.models import Develop
from member.models import Member
from django.utils import timezone


# Create your models here.

class Idea(models.Model):
    user = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='작성자', null=True)
    devtool = models.ForeignKey(Develop, on_delete=models.CASCADE, verbose_name='개발툴', null=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    interest = models.IntegerField(default=0)
    img_url = models.ImageField(upload_to='images/%Y%m%d', default='images/basic.jpg')
    created_date = models.DateTimeField('작성일', default=timezone.now)
