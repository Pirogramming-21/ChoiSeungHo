from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
# 로거 생성

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')

    return render(request, 'blog/post_list.html', {'posts': posts})
