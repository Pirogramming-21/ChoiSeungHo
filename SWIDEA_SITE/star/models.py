from django.db import models

from develop.models import Develop
from idea.models import Idea
from member.models import Member
from django.utils import timezone


# Create your models here.

class Star(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, verbose_name='북마크', null=True)
    created_date = models.DateTimeField('작성일', default=timezone.now)
