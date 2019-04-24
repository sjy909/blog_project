from django.shortcuts import render
from django.http import HttpResponse
from .models import ARTICLE, TALLY, COMMENT, KIND
from django.http import HttpResponseRedirect
import datetime
# Create your views here.


def index(request):
    articles = ARTICLE.objects.all().order_by("-date")
    tally = TALLY.objects.all()
    kind = KIND.objects.all()
    article_new_list = [articles[0], articles[1], articles[2]]
    date = datetime.date.today()
    return render(request, 'blog/index.html', {"articles": articles, "article_new_list": article_new_list,
                                               "tally": tally, "kind": kind, "date": date})


def single(request, i):
    article = ARTICLE.objects.get(pk=i)
    article.read_count += 1
    article.save()
    comments = article.comment_set.all()
    articles = ARTICLE.objects.all().order_by("-date")
    tally = TALLY.objects.all()
    kind = KIND.objects.all()
    article_new_list = [articles[0], articles[1], articles[2]]
    return render(request, "blog/single.html", {"i": i, "article": article, "comments": comments, "articles": articles, "article_new_list": article_new_list,
                                               "tally": tally, "kind": kind})


def comment(request, i):
    article = ARTICLE.objects.get(pk=i)
    comments = article.comment_set.all()
    c = COMMENT()
    c.c_a = article
    c.c_author = request.POST['name']
    c.c_content = request.POST['comment']
    c.save()
    return HttpResponseRedirect("/blog/single/%s/" % i, {"i": i, "article": article, "comments": comments})


def kinds(request, i):
    articles = ARTICLE.objects.all().order_by("-date")
    tally = TALLY.objects.all()
    kind = KIND.objects.all()
    article_new_list = [articles[0], articles[1], articles[2]]
    kinds = KIND.objects.get(pk=i)
    articles = kinds.article_set.all()
    return render(request, 'blog/index.html', {"articles": articles, "article_new_list": article_new_list,
                                               "tally": tally, "kind": kind})


def tallys(request, i):
    articles = ARTICLE.objects.all().order_by("-date")
    tally = TALLY.objects.all()
    kind = KIND.objects.all()
    article_new_list = [articles[0], articles[1], articles[2]]
    tallys = TALLY.objects.get(pk=i)
    articles = tallys.article_set.all()
    return render(request, 'blog/index.html', {"articles": articles, "article_new_list": article_new_list,
                                               "tally": tally, "kind": kind})


def date(request, y, m):
    articles = ARTICLE.objects.all().filter(date__year=y).filter(date__month=m)
    tally = TALLY.objects.all()
    kind = KIND.objects.all()
    if len(articles) > 2:
        article_new_list = [articles[0], articles[1], articles[2]]
    else:
        article_new_list = []
    date = datetime.date.today()
    return render(request, 'blog/index.html', {"articles": articles, "article_new_list": article_new_list,
                                               "tally": tally, "kind": kind, "date": date})
    # return HttpResponse("成功")
