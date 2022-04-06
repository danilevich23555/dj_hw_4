from django.shortcuts import render

from articles.models import Article, Scorpe, Relationship


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article_object = Article.objects.all().order_by(ordering)


    context = {
        'object_list': article_object
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
