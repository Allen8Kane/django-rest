from django.shortcuts import render

from django.http import HttpResponse
from .models import Article


def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.content for a in latest_article_list])
    print(output)
    return HttpResponse(output)


def detail(request, article_id):
    return HttpResponse("You're looking at question %s." % article_id)


def results(request, article_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % article_id)


def vote(request, article_id):
    return HttpResponse("You're voting on question %s." % article_id)
