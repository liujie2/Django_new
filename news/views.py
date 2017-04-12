from django.shortcuts import render
from django.http import HttpResponse
from news.models import *
# Create your views here.
def index(request):
    columns = Column.objects.all()
    return render(request, 'index.html', {'columns': columns})

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return HttpResponse('column slug: ' + column_slug)

def article_detail(request, article_slug):
    article = Article.objects.get(slug=article_slug)
    return HttpResponse('article slug: ' + article_slug)