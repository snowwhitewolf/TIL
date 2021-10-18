from community.models import Review
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ReviewForm
from django.views.decorators.http import require_POST,require_http_methods,require_safe
from django.contrib.auth.decorators import login_required
@require_safe
def index(request):
    movies = Review.objects.order_by('-pk')

    context = {
        'movies' : movies,
    }
    return render(request, 'community/index.html', context)

@require_safe
def detail(request,pk):
    movie = get_object_or_404(Review,pk=pk)
    context = {
        'movie':movie,
    }
    return render(request,'community/detail.html',context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail',review.pk)
    else:
        form = ReviewForm()
    context = {
        'form':form,
        'form_name':'CREATE',
    }
    return render(request,'community/form.html',context)

@login_required
@require_http_methods(['GET','POST'])
def update(request,pk):
    review = get_object_or_404(Review,pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST,instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail',review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form':form,
        'form_name':'UPDATE',
    }
    return render(request,'community/form.html',context)
@login_required
@require_POST
def delete(request,pk):
    if request.method == "POST":
        review = get_object_or_404(Review,pk=pk)
        review.delete()
    return redirect('community:index')