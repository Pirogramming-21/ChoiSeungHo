from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import Post, Comment, Like


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

    comments = Comment.objects.filter(post=pk).order_by('-created_at')
    count = post.likes.count()
    c_count = post.comments.count()
    context = {
        'post': post,
        'comments': comments,
        'count': count,
        'c_count': c_count
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
        comments = Comment.objects.get(id=pk)
        comments.delete()
        return JsonResponse({'id': 'zz'})


@csrf_exempt
def like(request):
    req = json.loads(request.body)
    post_id = req['id']
    Like.objects.create(post_id=post_id)
    return JsonResponse({'id': post_id})


@csrf_exempt
def comment(request):
    print('gd')
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            post_id = data['id']
            content = data.get('content', '')
            print(post_id, content)
            comments = Comment.objects.create(post_id=post_id, content=content)

            return JsonResponse({'id': comments.id, 'content': content})
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def like_ajax(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        post_id = req['id']
        button_type = req['type']

        post = Post.objects.get(id=post_id)

        if button_type == 'like':
            post.like += 1
        else:
            post.dislike += 1
        post.save()

    return JsonResponse({'id': post_id, 'type': button_type})
