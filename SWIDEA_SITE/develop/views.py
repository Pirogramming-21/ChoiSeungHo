from django.shortcuts import render, redirect

from idea.models import Idea
from .models import Develop
from .forms import DevelopForm


# Create your views here.

def main(request):
    develop = Develop.objects.all()
    context = {'develop': develop}

    return render(request, 'develop/list.html', context)


def create(request):
    form = DevelopForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('develop:main')
    form = DevelopForm()
    context = {'form': form}
    return render(request, 'develop/create.html', context)


def detail(request, pk):
    develop = Develop.objects.get(pk=pk)
    id_develop = Idea.objects.filter(devtool_id=pk)
    context = {'develop': develop,
               'id_tool': id_develop}
    return render(request, 'develop/detail.html', context)


def delete(request, pk):
    Develop.objects.get(pk=pk).delete()
    return redirect('develop:main')


def update(request, pk):
    develop = Develop.objects.get(pk=pk)
    form = DevelopForm(instance=develop)
    if request.method == 'POST':
        form = DevelopForm(request.POST, request.FILES, instance=develop)
        if form.is_valid():
            form.save()
            return redirect('develop:detail', pk=pk)

    context = {'pk': pk, 'form': form}
    return render(request, 'develop/update.html', context)
