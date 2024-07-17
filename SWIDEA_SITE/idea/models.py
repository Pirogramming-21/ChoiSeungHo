from django.db import models
from member.models import Member


# Create your models here.

class Idea(models.Model):
    DEVELOP_TOOL = [
        ('Spring', '스프링'),
        ('Django', '쟝고'),
        ('React', '리액트'),
        ('Flask', '플라스크'),
        ('Node.Js', '노드js'),
    ]
    user = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='작성자', null=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.CharField(max_length=10, choices=DEVELOP_TOOL, null=True)
    img_url = models.ImageField(upload_to='images/%Y%m%d', default='images/basic.jpg')
