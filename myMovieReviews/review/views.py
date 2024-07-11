from django.shortcuts import render, redirect

from review.models import Review


# Create your views here.

def home(request):
    review_list = Review.objects.all()

    context = {'review_list': review_list}
    return render(request, 'home.html', context)


def review_add(request):
    if request.method == 'POST':
        Review.objects.create(
            title=request.POST['title'],
            review=request.POST['review'],
            genre=request.POST['genre'],
            rate=request.POST['star'] + '점',
            movie_time=request.POST['movie_time'],
            director=request.POST['director'],
            actor=request.POST['actor'],
            year=request.POST['year']
        )
        return redirect('/')

    return render(request, 'review_add.html')


def review_detail(request, pk):
    review = Review.objects.get(id=pk)

    context = {'review': review}
    return render(request, 'review_detail.html', context)
