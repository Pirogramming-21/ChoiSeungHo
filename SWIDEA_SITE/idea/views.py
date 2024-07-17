from django.shortcuts import render, redirect

from idea.models import Idea
from star.models import Star
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
    sort = request.GET.get('sort', 'newest')
    query = request.GET.get('q', '')

    sort_order = {
        'star': 'star__created_date',
        'title': 'title',
        'newest': '-created_date',
        'oldest': 'created_date'
    }

    ideas = Idea.objects.all()
    if query:
        ideas = ideas.filter(title__icontains=query)

    if sort == 'star':
        # 외래키로 연결된 Star가 존재하는 Idea만 필터링
        ideas = ideas.filter(star__isnull=False).distinct()

    ideas = ideas.order_by(sort_order.get(sort, '-created_date'))

    paginator = Paginator(ideas, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    star = Star.objects.all()
    context = {'ideas': page_obj,
               'stars': star}
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
    star_exist = Star.objects.filter(idea=pk).exists()
    print(star_exist)
    context = {'idea': idea,
               'pk': pk,
               'star_exist': star_exist}
    return render(request, 'idea/detail.html', context)


def delete(request, pk):
    Idea.objects.get(pk=pk).delete()
    return redirect('idea:main')


def update(request, pk):
    idea = Idea.objects.get(pk=pk)

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea:detail', pk=pk)  # 저장 후 detail 뷰로 리디렉션
    else:
        form = IdeaForm(instance=idea)  # 기존 인스턴스로 폼 초기화

    context = {'pk': pk, 'form': form}
    return render(request, 'idea/update.html', context)
