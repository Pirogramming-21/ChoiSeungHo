from django.shortcuts import render, redirect

from review.models import Review


# Create your views here.

def home(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort_by', 'rate')

    review_list = Review.objects.all()
    if search_query:
        # 검색어가 제목에 포함된 리뷰를 필터링
        review_list = review_list.filter(title__icontains=search_query)

    # 정렬
    if sort_by == 'year':
        review_list = review_list.order_by('-year')
    elif sort_by == 'time':
        review_list = review_list.order_by('-movie_time')
    else:
        review_list = review_list.order_by('-rate')

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
            year=request.POST['year'],
            img_url=request.FILES['img_url']
        )
        return redirect('/')

    return render(request, 'review_add.html')


def review_detail(request, pk):
    review = Review.objects.get(id=pk)

    context = {'review': review}
    return render(request, 'review_detail.html', context)


def review_update(request, pk):
    reviews = Review.objects.get(id=pk)
    context = {'review': reviews}
    print(reviews.title)
    print(reviews.movie_time)
    if request.method == 'POST':
        reviews.title = request.POST['title']
        reviews.review = request.POST['review']
        reviews.genre = request.POST['genre']
        reviews.rate = request.POST['star'] + '점'
        reviews.movie_time = request.POST['movie_time']
        reviews.director = request.POST['director']
        reviews.actor = request.POST['actor']
        reviews.year = request.POST['year']
        reviews.img_url = request.FILES['img_url']
        reviews.save()
        return redirect(f'/review/{reviews.id}')
    return render(request, 'review_update.html', context)


def review_delete(request, pk):
    if request.method == 'POST':
        review = Review.objects.get(id=pk)
        review.delete()
        return redirect('/')
