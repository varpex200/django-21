from django.http import HttpResponse
from django.shortcuts import render
from articles.forms import CarForm

from articles.models import Article


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def retrieve(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
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