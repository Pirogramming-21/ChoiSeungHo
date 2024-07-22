from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import Post, Comment


# Create your views here.


def post_list(request):
    posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'list.html', context)


@csrf_exempt
def post_create(request):
    if request.method == 'POST':
        Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('/')

    return render(request, 'create.html')


def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    comment = Comment.objects.filter(post=pk)
    context = {
        'post': post,
        'comments': comment
    }
    return render(request, 'read.html', context)


@csrf_exempt
def post_update(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect(f'/{post.pk}/')
    return render(request, 'update.html', context)


@csrf_exempt
def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(id=pk)
        post.delete()
        return redirect('/')


@csrf_exempt
def comment_create(request, pk):
    if request.method == 'POST':
        posts = Post.objects.get(id=pk)
        Comment.objects.create(
            post=posts,
            content=request.POST['content']
        )
    return redirect(f'{pk}')


def comment_delete(request, pk):
    if request.method == 'POST':
        comment = Comment.objects.get(id=pk)
        comment.delete()
        return redirect('/')

# def like(request, pk):
