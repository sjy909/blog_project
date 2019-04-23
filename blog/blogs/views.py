from django.shortcuts import render
from django.http import HttpResponse
from .models import ARTICLE, TALLY, COMMENT, KIND
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    articles = ARTICLE.objects.all()
    tally = TALLY.objects.all()
    kind = KIND.objects.all()
    article_new_list = []
    for article in articles:
        if len(article_new_list) < 2:
            article_new_list.append(article)
        else:
            for a in article_new_list:
                if article.date > a.date:
                    article_new_list.remove(a)
                    article_new_list.append(article)
    return render(request, 'blog/index.html', {"articles": articles, "article_new_list": article_new_list,
                                               "tally": tally, "kind": kind})


def single(request, i):
    article = ARTICLE.objects.get(pk=i)
    comments = article.comment_set.all()
    print(comments)
    return render(request, "blog/single.html", {"i": i, "article": article, "comments": comments})


def comment(request, i):
    article = ARTICLE.objects.get(pk=i)
    comments = article.comment_set.all()
    c = COMMENT()
    c.c_a = article
    c.c_author = request.POST['name']
    c.c_content = request.POST['comment']
    c.save()
    return HttpResponseRedirect("/blog/single/%s/" % i, {"i": i, "article": article, "comments": comments})
