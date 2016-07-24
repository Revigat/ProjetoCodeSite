from django.conf.urls import url

urlpatterns = [
    url(r'^$','codesite.views.index'),
    url(r'^index','codesite.views.index', name='index'),
    #url(r'^apresenta/','codesite.views.apresenta'),
    url(r'^servicos/','codesite.views.servicos'),
    url(r'^cadastro/','codesite.views.cadastro'),
]