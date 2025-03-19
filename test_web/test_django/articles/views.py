from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm

# Create your views here.
# def index(request):
#     response = HttpResponse("<h1>Hello, Django!</h1>")
#     return response

def index(request):
    return render(request, "articles/index.html")

def data_throw(request):
    return render(request, "articles/data_throw.html")

def data_catch(request):
    message = request.GET.get("message")
    context = {"message" : message}
    return render(request, "articles/data_catch.html", context)

def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {
        "articles" : articles
    }
    return render(request, "articles/articles.html", context)


def article_detail(request, id):
    article = Article.objects.get(id=id)
    content = {
        "article" : article
    }
    return render(request, "articles/article_detail.html", content)


def create(request):
    if request.method == 'GET':
        form = ArticleForm
        context = {
            'form' : form
        }
        return render(request, "articles/create.html", context)
        
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
        return redirect("articles:articles")
    
    
    # title = request.POST.get("title")
    # content = request.POST.get("content")
    # article = Article.objects.create(title = title, content = content)
    
    
    # return redirect("article_detail", article.id)
    # return render(request, "create.html")


def delete(request, id):
    if request.method == 'GET':
        return redirect("articles:article_detail", article.id)
        
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        article.delete()
        return redirect("articles:articles")


def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
        context = {
            'form' : form,
            'article' : article,
        }
        return render(request, "articles/update.html", context)
        
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
        return redirect("articles:article_detail", article.id)
