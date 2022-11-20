from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_def
from django.contrib.auth.decorators import login_required
from articles.forms import CarForm, ArticleForm, CommentForm

from articles.models import Article

@login_required
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

@login_required
def retrieve(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.save()
    else:
        form = ArticleForm(instance=article)
        comment_form = CommentForm(initial={
            'related_article': id,
            'related_user': request.user.id
        })
    context = {
        'article': article,
        'form': form,
        'comment_form': comment_form
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

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login_def(request, user)
            return redirect('/')

    return render(request, 'login.html')