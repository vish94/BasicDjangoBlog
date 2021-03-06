from django.http import HttpResponse
from django.shortcuts import render_to_response
from articles.models import Article
from articles.models import Comment
from forms import ArticleForm
from forms import CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.
def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {}
    args.update(csrf(request))
    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render_to_response('articles.html', args)

def article(request, article_id=1):
    form = CommentForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comment.objects.filter(article_id=article_id)
    
    return render_to_response('article.html', args)
                            

def language(request, language='em-gn'):
    response = HttpResponse("setting language to "+language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response


def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html', args);

def like_article(request, article_id=0):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count = count + 1
        a.likes = count
        a.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)

def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = Article.objects.filter(title__contains=search_text)
    return render_to_response('ajax_search.html', {'articles': articles})

def add_comment(request, article_id=0):
    if article_id and request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_id = article_id
            comment.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)

    
