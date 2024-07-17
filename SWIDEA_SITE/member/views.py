from django.shortcuts import render, redirect

from member.forms import MemberForm


# Create your views here.
def create(request):
    if request.method == 'GET':
        form = MemberForm()
        context = {'form': form}
        return render(request, 'member/create.html', context)
    form = MemberForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('idea:main')
