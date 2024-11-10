from django.urls import path
from .views import home, ArticleDetailView, noticias_view, warnings_view, contact, tips_view

urlpatterns = [
    path('', home, name='home'),
    path('<str:tipo>/<slug:slug>/',
         ArticleDetailView.as_view(), name='artigo_detail'),
    path('noticias/', noticias_view, name='noticias'),
    path('avisos/', warnings_view, name='avisos'),
    path('dicas/', tips_view, name='dicas'),
    path('contato/', contact, name='avisos'),
]
