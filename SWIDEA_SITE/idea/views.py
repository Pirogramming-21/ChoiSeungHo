from django.shortcuts import render, redirect

from idea.models import Idea
from .forms import IdeaForm


# Create your views here.

def main(request):
    idea = Idea.objects.all()
    context = {'idea', idea}

    return render(request, 'idea/list.html', context)


def create(request):
    form = IdeaForm(request.post, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('idea:main')


def detail(request, pk):
    idea = Idea.objects.get(pk=pk)
    context = {'idea': idea}
    return render(request, 'idea/detail.html', context)


def delete(request, pk):
    Idea.objects.get(pk=pk).delete()
    return redirect('idea:main')


def update(request, pk):
    idea = Idea.objects.get(pk=pk)
    form = IdeaForm(instance=idea)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea:detail', pk=pk)

    context = {'pk': pk, 'form': form}
    return render(request, 'idea/detail.html', context)
