from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, 'about.html')