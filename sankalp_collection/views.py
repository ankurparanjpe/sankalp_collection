from django.shortcuts import render
from django.http import HttpResponse
from .models import articles, ArticleCategory


def link(request, link):
    link = articles.objects.get(link=link)
    return render(request, 'sankalpcollection/single_article.html', {'link': link})


def category_link(request, category_link):
    category = ArticleCategory.objects.get(category_link=category_link)
    return render(request, 'sankalpcollection/articles.html', {'category': category,
                                                               'articles': articles.objects.all})


def homepage(request):
    art_cat = ArticleCategory.objects.all()
    return render(request, 'sankalpcollection/home.html', {'category': ArticleCategory.objects.all,
                                                           'articles': articles.objects.all})
