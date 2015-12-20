from django.conf.urls import include, url

urlpatterns = [
    url(r'^all/$', 'articles.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'articles.views.article'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'articles.views.language'),
    url(r'^create/$', 'articles.views.create'),
    url(r'^like/(?P<article_id>\d+)/$', 'articles.views.like_article'),
    url(r'^search/$', 'articles.views.search_titles'),
    url(r'^addcomment/(?P<article_id>\d+)/$', 'articles.views.add_comment'),
]
