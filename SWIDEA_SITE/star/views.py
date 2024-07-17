from django.shortcuts import render, redirect

from idea.models import Idea
from .models import Star


def push(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(pk=pk)
        Star.objects.create(idea=idea)
    return redirect('idea:detail', pk=pk)


def delete(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(pk=pk)
        Star.objects.filter(idea=idea).delete()
        print("gd")
    return redirect('idea:detail', pk=pk)
