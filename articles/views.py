from django.http import HttpResponse
from django.shortcuts import render
from articles.forms import CarForm, ArticleForm

from articles.models import Article


def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm()
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'form': form
    }
    return render(request, 'index.html', context)

def retrieve(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'retrieve.html', context)

def about(request):
    if request.method == 'POST':
        form = CarForm(request.POST or None)
        if form.is_valid():
            form.save()
    form = CarForm()
    context = {
        'form': form
    }
    return render(request, 'about.html', context)