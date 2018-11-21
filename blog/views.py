from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import BlogArticles


# Create your views here.
@login_required(login_url='/accounts/login/')
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})


@login_required(login_url='/accounts/login/')
def blog_articles(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})
