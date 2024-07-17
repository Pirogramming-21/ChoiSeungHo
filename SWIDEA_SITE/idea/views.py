from django.shortcuts import render, redirect

from idea.models import Idea
from .forms import IdeaForm
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
@csrf_exempt
def change_interest(request):
    if request.method == 'POST':
        idea_id = request.POST.get('idea_id')
        action = request.POST.get('action')

        try:
            idea = Idea.objects.get(id=idea_id)
            if action == 'increase':
                idea.interest += 1
            elif action == 'decrease':
                idea.interest -= 1
            idea.save()

            return JsonResponse({'new_interest': idea.interest})
        except Idea.DoesNotExist:
            return JsonResponse({'error': 'Idea not found'}, status=404)

    return JsonResponse({'error': 'Invalid request'}, status=400)


def main(request):
    sort = request.GET.get('sort', 'interest')
    query = request.GET.get('q', '')

    sort_order = {
        'interest': '-interest',
        'title': 'title',
        'newest': '-created_date',
        'oldest': 'created_date'
    }

    ideas = Idea.objects.all()
    if query:
        ideas = ideas.filter(title__icontains=query)

    ideas = ideas.order_by(sort_order.get(sort, '-interest'))

    paginator = Paginator(ideas, 4)  # 페이지당 4개의 아이디어를 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'ideas': page_obj, 'request': request}
    return render(request, 'idea/list.html', context)


def create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('idea:main')
    form = IdeaForm()
    context = {'form': form}
    return render(request, 'idea/create.html', context)


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
